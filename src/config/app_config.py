from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

# App variables
APP_DEBUG = os.environ.get("FLASK_DEBUG") or 0
APP_PORT = os.environ.get("CONFIG_PORT") or 5000

# Database variables
DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_NAME = os.environ.get("POSTGRES_DB")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_HOST = os.environ.get("POSTGRES_HOST")
STATIC_TOKEN = os.environ.get("STATIC_TOKEN")
DATABASE_URL = (f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

database = SQLAlchemy()

def init_db(app):
    try:
        database.init_app(app)
        database.create_all()
    except Exception as e:
        print(e)

def config_app(app):
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    app_context = app.app_context()
    app_context.push()
