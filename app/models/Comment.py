import app.db as db
import json

class Comment(db.Document):
    post = db.ReferenceField(Post, dbref=False, reverse_delete_rule=PULL)
    user = db.ReferenceField(User, dbref=False, reverse_delete_rule=PULL)
    username = db.StringField(min_length=1, max_length=24, default='anonymous')
    image_url = db.URLField(required=False)
    reply_comment = db.ReferenceField(Comment, dbref=False, required=False)
    text = db.StringField(max_length=1024)