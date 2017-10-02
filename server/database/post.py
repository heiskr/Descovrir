from framework.elasticsearch import es
from modules.util import json_prep, pick
from schemas.post import schema as post_schema
from schemas.proposal import schema as proposal_schema
from schemas.vote import schema as vote_schema
from database.util import deliver_fields
from database.util import insert_row, update_row, get_row, list_rows
from modules.util import convert_slug_to_uuid, convert_uuid_to_slug


def get_post_schema(data):
    kind = data.get('kind')
    mapping = {
        'post': post_schema,
        'proposal': proposal_schema,
        'vote': vote_schema,
    }
    return mapping.get(kind) or post_schema


def is_valid_reply(db_conn, data):
    """
    For Post, Proposal, Vote.

    A reply must belong to the same topic.
    - A post can reply to a post, proposal, or vote.
    - A proposal can reply to a post, proposal, or vote.
    - A vote may only reply to a proposal.
    """

    if data.get('replies_to_id'):
        post_data = get_post(db_conn, {'id': data['replies_to_id']})
        if post_data['topic_id'] != data['topic_id']:
            return [{'message': 'A reply must be in the same topic.'}]
    return []


def validate_entity_versions(db_conn, data):
    """
    For Proposal.

    Ensure all the entity versions exist.
    """

    from database.entity_facade import get_entity_version

    for p_entity_version in data['entity_versions']:
        entity_kind = p_entity_version.get('kind')
        version_id = p_entity_version.get('id')
        entity_version = get_entity_version(db_conn, entity_kind, version_id)
        if not entity_version:
            return [{
                'name': 'entity_versions',
                'message': 'Not a valid version: {entity_kind} {version_id}'
                .format(
                    entity_kind=entity_kind,
                    version_id=version_id
                ),
            }]
    return []


def is_valid_reply_kind(db_conn, data):
    """
    For Vote.

    A vote can reply to a proposal.
    A vote cannot reply to a proposal that is accepted or declined.
    A user cannot vote on their own proposal.
    """

    from database.entity_facade import get_entity_version

    proposal_data = get_post(db_conn, {'id': data['replies_to_id']})
    if not proposal_data:
        return [{'message': 'No proposal found.'}]
    if proposal_data['kind'] != 'proposal':
        return [{'message': 'A vote must reply to a proposal.'}]
    if proposal_data['user_id'] == data['user_id']:
        return [{'message': 'You cannot vote on your own proposal.'}]
    entity_kind = proposal_data['entity_versions'][0]['kind']
    version_id = proposal_data['entity_versions'][0]['id']
    entity_version = get_entity_version(db_conn, entity_kind, version_id)
    if not entity_version:
        return [{'message': 'No entity version for proposal.'}]
    if entity_version['status'] in ('accepted', 'declined'):
        return [{'message': 'Proposal is already complete.'}]
    return []


def insert_post(db_conn, data):
    """
    Create a new post.
    """

    schema = get_post_schema(data)
    query = """
        INSERT INTO posts
        (  user_id  ,   topic_id  ,   kind  ,   body  ,   replies_to_id  )
        VALUES
        (%(user_id)s, %(topic_id)s, %(kind)s, %(body)s, %(replies_to_id)s)
        RETURNING *;
    """
    data = {
        'user_id': convert_slug_to_uuid(data['user_id']),
        'topic_id': convert_slug_to_uuid(data['topic_id']),
        'kind': data['kind'],
        'body': data.get('body'),
        'replies_to_id': data.get('replies_to_id'),
    }
    if not data.get('replies_to_id'):
        data['replies_to_id'] = None
    errors = is_valid_reply(db_conn, data)
    if errors:
        return None, errors
    data, errors = insert_row(db_conn, schema, query, data)
    if not errors:
        add_post_to_es(db_conn, data)
    return data, errors


def insert_proposal(db_conn, data):
    """
    Create a new proposal.
    """

    schema = get_post_schema(data)
    query = """
        INSERT INTO posts
        (  user_id  ,   topic_id  ,   kind  ,   body  ,
           replies_to_id  ,   entity_versions  )
        VALUES
        (%(user_id)s, %(topic_id)s, %(kind)s, %(body)s,
         %(replies_to_id)s, %(entity_versions)s)
        RETURNING *;
    """
    data = {
        'user_id': convert_slug_to_uuid(data['user_id']),
        'topic_id': convert_slug_to_uuid(data['topic_id']),
        'kind': data['kind'],
        'body': data.get('body'),
        'replies_to_id': data.get('replies_to_id'),
        'entity_versions': data['entity_versions'],
    }
    errors = is_valid_reply(db_conn, data)
    if errors:
        return None, errors
    errors = validate_entity_versions(db_conn, data)
    if errors:
        return None, errors
    data, errors = insert_row(db_conn, schema, query, data)
    if not errors:
        add_post_to_es(db_conn, data)
    return data, errors


def insert_vote(db_conn, data):
    """
    Create a new vote.
    """

    schema = get_post_schema(data)
    query = """
        INSERT INTO posts
        (  user_id  ,   topic_id  ,   kind  ,   body  ,
           replies_to_id  ,   response  )
        VALUES
        (%(user_id)s, %(topic_id)s, %(kind)s, %(body)s,
         %(replies_to_id)s, %(response)s)
        RETURNING *;
    """
    data = {
        'user_id': convert_slug_to_uuid(data['user_id']),
        'topic_id': convert_slug_to_uuid(data['topic_id']),
        'kind': data['kind'],
        'body': data.get('body'),
        'replies_to_id': data.get('replies_to_id'),
        'response': data['response'],
    }
    errors = is_valid_reply(db_conn, data)
    if errors:
        return None, errors
    errors = is_valid_reply_kind(db_conn, data)
    if errors:
        return None, errors
    data, errors = insert_row(db_conn, schema, query, data)
    if not errors:
        add_post_to_es(db_conn, data)
    return data, errors


def update_post(db_conn, prev_data, data):
    """
    Update an existing post.
    """

    schema = get_post_schema(data)
    query = """
        UPDATE posts
        SET body = %(body)s
        WHERE id = %(id)s AND kind = 'post'
        RETURNING *;
    """
    data = {
        'id': convert_slug_to_uuid(prev_data['id']),
        'body': data['body'],
    }
    data, errors = update_row(db_conn, schema, query, prev_data, data)
    if not errors:
        add_post_to_es(db_conn, data)
    return data, errors


def update_proposal(db_conn, prev_data, data):
    """
    Update an existing proposal.
    """

    schema = get_post_schema(data)
    query = """
        UPDATE posts
        SET body = %(body)s
        WHERE id = %(id)s AND kind = 'proposal'
        RETURNING *;
    """
    data = {
        'id': convert_slug_to_uuid(prev_data['id']),
        'body': data['body'],
    }
    data, errors = update_row(db_conn, schema, query, prev_data, data)
    if not errors:
        add_post_to_es(db_conn, data)
    return data, errors


def update_vote(db_conn, prev_data, data):
    """
    Update an existing vote.
    """

    schema = get_post_schema(data)
    query = """
        UPDATE posts
        SET body = %(body)s, response = %(response)s
        WHERE id = %(id)s AND kind = 'vote'
        RETURNING *;
    """
    data = {
        'id': convert_slug_to_uuid(prev_data['id']),
        'body': data['body'],
        'response': data['response'],
    }
    data, errors = update_row(db_conn, schema, query, prev_data, data)
    if not errors:
        add_post_to_es(db_conn, data)
    return data, errors


def get_post(db_conn, params):
    """
    Get the post matching the parameters.
    """

    query = """
        SELECT *
        FROM posts
        WHERE id = %(id)s
        LIMIT 1;
    """
    params = {
        'id': convert_slug_to_uuid(params['id']),
    }
    return get_row(db_conn, query, params)


def list_posts_by_topic(db_conn, params):
    """
    Get a list of posts in Sagefy.
    """

    query = """
        SELECT *
        FROM posts
        WHERE topic_id = %(topic_id)s
        ORDER BY created ASC;
        /* TODO OFFSET LIMIT */
    """
    params = {
        'topic_id': convert_slug_to_uuid(params['topic_id']),
    }
    return list_rows(db_conn, query, params)


def list_posts_by_user(db_conn, params):
    """
    Get a list of posts in Sagefy.
    """

    query = """
        SELECT *
        FROM posts
        WHERE user_id = %(user_id)s
        ORDER BY created ASC;
        /* TODO OFFSET LIMIT */
    """
    params = pick(params, ('user_id',))
    return list_rows(db_conn, query, params)


def deliver_post(data, access=None):
    """
    Prepare post data for JSON response.
    """

    schema = get_post_schema(data)
    return deliver_fields(schema, data, access)


def add_post_to_es(db_conn, post):
    """
    Upsert the post data into elasticsearch.
    """

    from database.topic import get_topic, deliver_topic
    from database.user import get_user, deliver_user

    data = json_prep(deliver_post(post))
    topic = get_topic(db_conn, {'id': post['topic_id']})
    if topic:
        data['topic'] = json_prep(deliver_topic(topic))
    user = get_user(db_conn, {'id': post['user_id']})
    if user:
        data['user'] = json_prep(deliver_user(user))

    return es.index(
        index='entity',
        doc_type='post',
        body=data,
        id=convert_uuid_to_slug(post['id']),
    )


def list_votes_by_proposal(db_conn, proposal_id):
    """
    List votes for a given proposal.
    """

    query = """
        SELECT *
        FROM posts
        WHERE kind = 'vote' AND replies_to_id = %(proposal_id)s
        ORDER BY created DESC;
        /* TODO OFFSET LIMIT */
    """
    params = {
        'proposal_id': convert_slug_to_uuid(proposal_id),
    }
    return list_rows(db_conn, query, params)
