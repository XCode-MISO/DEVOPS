from dotenv import load_dotenv, find_dotenv
from flask import Flask, request

from src.views.views  import post_add_email_to_blacklist, get_blacklisted_entries
from src.config.app_config import config_app, init_db, database, APP_DEBUG, APP_PORT

# Load environment variables
env_file = find_dotenv('.env.development')
load_dotenv(env_file)

# App configuration
application = Flask(__name__)
config_app(application)

# Database initialization
init_db(application)

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
