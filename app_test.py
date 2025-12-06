import pytest
from app import app as flask_app

@pytest.fixture
def app():
    return flask_app

def test_get_article(client):
    response = client.get('/article/no-article')
    assert response.status_code == 404