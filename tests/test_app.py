import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server.app import app

def test_index_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"<html" in response.data

def test_api_data_success():
    client = app.test_client()
    response = client.get('/api/data')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)
    assert "message" in data
    assert data["status"] == "success"

def test_api_data_content_type():
    client = app.test_client()
    response = client.get('/api/data')
    assert response.content_type == 'application/json'

def test_api_data_structure():
    client = app.test_client()
    response = client.get('/api/data')
    data = response.get_json()

    # These will fail initially because the route and function don't exist
    assert isinstance(data["message"], str)
    assert isinstance(data["status"], str)

