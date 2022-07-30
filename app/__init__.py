from app.routes import api
from flask import Flask
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv
import os

def create_app(test_config=None):
    load_dotenv
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False 
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET')
    )
    app.config['MONGODB_SETTINGS'] = {
        'db': os.getenv('DB_NAME'),
        'host': os.getenv('HOST'),
        'port': os.getenv('PORT')
    }
    db = MongoEngine()
    db.init_app(app)

    return app