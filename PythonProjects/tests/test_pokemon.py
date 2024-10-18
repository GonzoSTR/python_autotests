import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c25aedc9ef1ca7d0862dd14969b3a27f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRANER_ID = '11147'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id': TRANER_ID})
    assert response.status_code == 200

def test_name_trainer():
    response_get = requests.get(url = f'{URL}/trainers', params={'trainer_id': TRANER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Слуцкий Леонид'
