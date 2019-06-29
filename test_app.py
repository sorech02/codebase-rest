import pytest

from app import app

@pytest.fixture
def client():
    client = app.test_client()

    yield client

def test_get_all_cvx(client):
    response = client.get('/codeset/cvx')
    assert b'Adenovirus' in response.data
    assert 'cvxs' in response.json

def test_get_cvx(client):
    response = client.get('/codeset/cvx/143')
    assert b'Adenovirus' in response.data
    print(response.json)
    assert 'Adenovirus' in response.json['cvx']['description']

def test_get_bad_cvx(client):
    response = client.get('/codeset/cvx/1')
    assert b'error' in response.data
    assert 404 == response.status_code
