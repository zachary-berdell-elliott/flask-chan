import app.db as db
import json

class CommentUpvote(db.Document):
    user = db.ReferenceField(User, dbref=False, reverse_delete_rule=PULL)
    comment = db.ReferenceField(Comment, dbref=False, reverse_delete_rule=PULL)
    upvote = db.BooleanField(required=True, default=False)
    downvote = db.BooleanField(required=True, default=False)