import app.db as db
import json
from .Post import Post

class Category(db.Document):
    name = db.StringField(min_length=1, maxlength=12, required=True)
    posts = db.ReferenceField(Post, dbref=False, reverse_delete_rule=CASCADE)
    isNSFW = db.BooleanField(default=False)
