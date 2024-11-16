from flask import Flask, request
from src.views.views import post_add_email_to_blacklist, get_blacklisted_entries
from src.config.app_config import config_app, init_db, database, APP_DEBUG, APP_PORT
import os

application = Flask(__name__)

config_app(application)
init_db(application)

@application.route("/", methods=["GET"])
def app_main():
    return {"msg": "app runnging"}, 200

@application.route("/params", methods=["GET"])
def app_params():
    DB_HOST = os.environ.get("POSTGRES_HOST")
    DB_USER = os.environ.get("POSTGRES_USER")
    DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    DB_NAME = os.environ.get("POSTGRES_DB")
    DB_PORT = os.environ.get("POSTGRES_PORT")
    DB_HOST = os.environ.get("POSTGRES_HOST")
    STATIC_TOKEN = os.environ.get("STATIC_TOKEN", 'static_token')
    ENVIRONMENT = os.getenv("ENVIRONMENT")
    return {"DB_HOST": DB_HOST, "DB_USER": DB_USER, "DB_PASSWORD": DB_PASSWORD, "DB_NAME": DB_NAME, "DB_PORT": DB_PORT, "DB_HOST": DB_HOST, "STATIC_TOKEN": STATIC_TOKEN, "ENVIRONMENT": ENVIRONMENT}, 200

@application.route("/health", methods=["GET"])
def check_service():
    return {"msg": "Healthy"}, 200

@application.route("/blacklists", methods=["POST"])
def add_email_to_blacklist():
    return post_add_email_to_blacklist(database, request)

@application.route("/blacklists/<email>", methods=["GET"])
def get_blacklisted_entries_route(email):
    return get_blacklisted_entries(database, request, email)

if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=APP_DEBUG, port=APP_PORT)
