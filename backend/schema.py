from marshmallow import Schema, fields, validate

class AdSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    media_type = fields.Str(required=True, validate=validate.OneOf(['audio', 'video']))
    duration = fields.Str(required=True)

class ChannelSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    media_type = fields.Str(required=True, validate=validate.OneOf(['tv', 'radio']))
    folder_path = fields.Str(required=True)
    is_active = fields.Boolean()

class SettingSchema(Schema):
    default_media_type = fields.Str(validate=validate.OneOf(['audio', 'video']))
    notification_email = fields.Email()
    data_retention_days = fields.Int(validate=validate.Range(min=1))
    confidence_threshold = fields.Float(validate=validate.Range(min=0, max=1))