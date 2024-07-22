import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'сюда вставляешь свой токен'
HEADER = {'Content-Type':'application/json' , 'trainer_token':TOKEN}
TRAINER_ID = '4203'

def test_status_code():
    response = requests.get(url = f'{URL}/v2/trainers' , headers = HEADER)
    assert response.status_code == 200 

def test_check_name():
    respose_check = requests.get(url = f'{URL}/v2/trainers' , headers = HEADER , params = {'trainer_id' : TRAINER_ID})
    assert respose_check.json()["data"][0]["trainer_name"] == 'PikaLover'