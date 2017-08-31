schema = {
    'tablename': '',
    'fields': {
        'id': {},
        'created': {},
        'modified': {},
    },
    'validate': tuple(),
}


# Extend with: schema = extend({}, parentSchema, { ... })

# Avaliable per field:
# - validate:   a list of functions to run on the field.
#               return a string if error, None if okay
# - bundle:     before saving to the database,
#               transform the data
#               bundle happens AFTER validate. be careful!
# - default:    default value of the field
#               can be a value or a function to call
# - deliver:    tranform the data before sending out to the client
#               can also be used for permissions
# - access:     control which client can access this field's information
# - unique:     True will check to make sure no other row has
#               the same value not needed on `id` field,
#               as it is the primary key
# - embed:      list of fields contained in the field
# - embed_many: list of fields contained in a list of dicts
