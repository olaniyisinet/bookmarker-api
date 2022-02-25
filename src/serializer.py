from marshmallow import Schema,fields

class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    email = fields.String()
    created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    updated_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')

class BookmarkSchema(Schema):
    id = fields.Integer()
    body = fields.String()
    url = fields.String()
    short_url = fields.String()
    visits = fields.Integer()
    # user_id = fields.Integer()
    created_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    updated_at = fields.DateTime('%Y-%m-%dT%H:%M:%S')
    user = fields.Nested(lambda: UserSchema(only=("email", "username", "id")))
