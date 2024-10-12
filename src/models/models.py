from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import DateTime
from datetime import datetime
from src.config.app_config import database

def get_time():
    return datetime.now().isoformat()

class Blacklisted(database.Model):
    __tablename__ = "blacklisted"
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String, unique=True, nullable=False)
    app_uuid = database.Column(database.String, nullable=False)
    blocked_reason = database.Column(database.String(255), nullable=True)
    ip_address = database.Column(database.String, nullable=False)
    time = database.Column(DateTime, default=get_time(), nullable=False)

    def __init__(
        self,
        email,
        app_uuid,
        blocked_reason,
        ip_address,
        time,
    ):
        self.email = email
        self.app_uuid = app_uuid
        self.blocked_reason = blocked_reason
        self.ip_address = ip_address
        self.time = time

class BlacklistedSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Blacklisted
        load_instance = True

    email = fields.String()
    app_uuid = fields.String()
    blocked_reason = fields.String()
    ip_address = fields.String()
    time = fields.String()
