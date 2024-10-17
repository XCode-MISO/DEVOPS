import os
import pytest
from application import application
from src.config.app_config import init_db

@pytest.fixture
def test_app():
    init_db(application)
    with application.app_context():
        yield application

@pytest.fixture
def client(test_app):
    return test_app.test_client()
