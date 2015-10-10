from modules.validations import is_required, is_string
from models.post import Post


class Proposal(Post):
    """A proposal to change the discussed entity."""

    schema = dict(Post.schema.copy(), **{
        'entity_version_id': {
            'validate': (is_required, is_string,)
        },
        'name': {
            'validate': (is_required, is_string,)
        },
    })

    def __init__(self, fields=None):
        """

        """
        super().__init__(fields)
        self.kind = 'proposal'

    def validate(self):
        errors = super().validate()
        if not errors:
            errors += self.is_valid_reply_kind()
        if not errors:
            errors += self.is_valid_version()
        return errors

    def is_valid_reply_kind(self):
        """
        TODO@ A proposal can reply to post, proposal, or flag.
        """
        return []

    def is_valid_version(self):
        """
        TODO@ Ensure this is a valid version of the entity.
        """
        return []