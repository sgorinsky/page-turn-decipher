import pytest
# from static.tests import MOCK_DATA
from page_turn_decipher.router import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        with app.test_client() as client:
            yield client


def test_make_prediction__fake_long_article(client):
    response = client.get('health')
    print(response.__dir__())
    assert response.data == b'success'
    assert response.status_code == 200


def test_make_prediction__fake_short_article(client):
    response = client.get('health')
    print(response.__dir__())
    assert response.data == b'success'
    assert response.status_code == 200
    

def test_make_prediction__real_long_article(client):
    response = client.get('health')
    print(response.__dir__())
    assert response.data == b'success'
    assert response.status_code == 200


def test_make_prediction__real_short_article(client):
    response = client.get('health')
    print(response.__dir__())
    assert response.data == b'success'
    assert response.status_code == 200

    
    
