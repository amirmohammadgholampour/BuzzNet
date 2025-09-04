from mongoengine import Document, StringField, ReferenceField, DateTimeField
import datetime

class PostMeta(Document):
    post_id = StringField(required=True)
    tags = StringField()
    device = StringField()
    location = StringField()
    created_at = DateTimeField(default=datetime.datetime.utcnow)

    meta = {"collection": "post_meta"}