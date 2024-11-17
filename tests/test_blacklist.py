import os
import json
import pytest
from application import application
from datetime import datetime

STATIC_TOKEN = os.getenv("STATIC_TOKEN", "valid_token_for_testing")

@pytest.fixture
def test_app():
    with application.app_context():
        yield application

@pytest.fixture
def client(test_app):
    return test_app.test_client()

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 400
    assert response.get_json() == {"msg": "Healthy"}

def test_add_email_to_blacklist(client):
    headers = {
        'Authorization': f'Bearer {STATIC_TOKEN}'
    }
    data = {
        'email': 'test@example.com',
        'app_uuid': '12345',
        'blocked_reason': 'Spam activity'
    }
    response = client.post('/blacklists', headers=headers, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    assert 'id' in response.get_json()
    assert 'createdAt' in response.get_json()

def test_add_email_to_blacklist_unauthorized(client):
    data = {
        'email': 'test@example.com',
        'app_uuid': '12345',
        'blocked_reason': 'Spam activity'
    }
    response = client.post('/blacklists', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert response.get_json() == {"msg": "Authorization header is not in the headers or bearer value is wrong"}

def test_get_blacklisted_entries(client):
    headers = {
        'Authorization': f'Bearer {STATIC_TOKEN}'
    }
    data = {
        'email': 'test@example.com',
        'app_uuid': '12345',
        'blocked_reason': 'Spam activity'
    }
    # First add the email to the blacklist
    client.post('/blacklists', headers=headers, data=json.dumps(data), content_type='application/json')
    # Now get the blacklisted entry
    response = client.get('/blacklists/test@example.com', headers=headers)
    assert response.status_code == 200
    assert response.get_json() == {
        "blacklisted": True,
        "blocked_reason": "Spam activity"
    }

def test_get_blacklisted_entries_not_found(client):
    headers = {
        'Authorization': f'Bearer {STATIC_TOKEN}'
    }
    response = client.get('/blacklists/notfound@example.com', headers=headers)
    assert response.status_code == 200
    assert response.get_json() == {
        "blacklisted": False,
        "blocked_reason": ""
    }
