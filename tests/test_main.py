import pytest
import sys
import os

# Ajoute le dossier parent au path pour importer app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import add_numbers, app

def test_add_numbers():
    """Test de la fonction add_numbers"""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_hello_endpoint():
    """Test de l'endpoint hello"""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'success'

def test_health_endpoint():
    """Test de l'endpoint health"""
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'