import app.db as db
import json

class Post(db.Document):
    user = db.ReferenceField(User, dbref=False, reverse_delete_rule=PULL)
    username = db.StringField(min_length=1, max_length=24, default='anonymous')
    image_url = db.URLField(required=True)
    title = db.StringField(required=True, min_length=1, max_length=32)
    text = db.StringField(max_length=2048)
    upvotes = db.ListField(field=db.ReferenceField(Upvote, dbref=False, reverse_delete_rule=CASCADE))
    comments = db.ListField(field=db.ReferenceField(Comment, dbref=False, reverse_delete_rule=CASCADE))
    