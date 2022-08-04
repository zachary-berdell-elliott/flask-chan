import app.db as db
import json

class User(db.document):
    username = db.StringField(required=true, mion_length=1, max_length=48)
    posts = db.ListField(field=db.ReferenceField(Post, dbref=False, reverse_delete_rule=CASCADE))
    comments = db.ListField(field=db.ReferenceField(Comment, dbref=False, reverse_delete_rule=CASCADE))
    upvotes = db.ListField(field=db.ReferenceField(Upvote, dbref=False, reverse_delete_rule=CASCADE))
    is_moderator = db.BooleanField(default=False)
    created_at = db.DateTimeField(default=datetime.now())