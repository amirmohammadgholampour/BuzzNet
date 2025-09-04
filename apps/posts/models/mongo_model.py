from mongoengine import Document, StringField, DateTimeField, IntField
import datetime

class PostMeta(Document):
    post_id = IntField(required=True)
    tags = StringField()
    device = StringField()
    location = StringField()
    created_at = DateTimeField(default=datetime.datetime.utcnow)

    meta = {"collection": "post_meta"}