from dotenv import load_dotenv, find_dotenv
from flask import Flask, request

#from src.endpoints.blacklist import post_add_email_to_blacklist, blackmail_info_get
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

if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=APP_DEBUG, port=APP_PORT)
