from datetime import datetime

from src.models.models import Blacklisted, BlacklistedSchema
from src.config.app_config import STATIC_TOKEN

def validate_token(bearer):
    if bearer is None or bearer == "":
        return {
            "msg": "Authorization header is not in the headers or bearer value is wrong"
        }, 400
    if len(bearer.split()) < 2:
        return {"msg": "Token is not in the headers"}, 400

    token = bearer.split()[1]

    if token != STATIC_TOKEN:
        return {"msg": "Unauthorized"}, 401
    return {}, 200

def post_add_email_to_blacklist(db, request):
    try:
        data = request.get_json()

        bearer = request.headers.get("Authorization")
        validationError, errorCode = validate_token(bearer)
        if errorCode != 200:
            return validationError, errorCode
        
        email = data["email"]
        if str(email) == "":
            return {"msg": "The email is missing, please provide a valid email"}, 400

        existing_email = db.session.query(Blacklisted).filter_by(email=email).first()
        if existing_email:
            return {"msg": "This email was already blacklisted"}, 400

        app_uuid = data["app_uuid"]
        if str(app_uuid) == "":
            return {
                "msg": "The app_uuid is missing, please provide a valid app id"
            }, 400

        blocked_reason = data["blocked_reason"]
        if len(blocked_reason) > 255:
            return {"msg": "The block reason has to be less than 255 characters"}, 400

        ip_address = str(request.remote_addr)

        new_blacklisted = Blacklisted(
            email=email,
            app_uuid=app_uuid,
            blocked_reason=blocked_reason,
            ip_address=ip_address,
            time=datetime.now().isoformat(),
        )

        db.session.add(new_blacklisted)
        db.session.commit()
        BlacklistedSchema().dump(new_blacklisted)
        return {
            "id": new_blacklisted.id,
            "createdAt": new_blacklisted.time.isoformat(),
        }, 201
    except Exception as e:
        print(e)
        return {"msg": str(e)}, 500


def get_blacklisted_entries(db, request, email):
    try:

        bearer = request.headers.get("Authorization")

        validError, errorCode = validate_token(bearer)
        if errorCode != 200:
            return validError, errorCode

        if str(email) == "":
            return {"msg": "The email is missing, please provide an email"}, 400

        try:
            blackmailed = db.session.query(Blacklisted).filter_by(email=email).first().__dict__
            return {"blacklisted": True, "blocked_reason": str(blackmailed["blocked_reason"])}, 200
        except Exception as e:
            print(e)
            return {"blacklisted": False, "blocked_reason": ""}, 200

    except Exception as e:
        return {"msg": str(e)}, 500