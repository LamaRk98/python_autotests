import requests 
import pytest

token = "0b5b90debcebef2207b97642b5a01311"
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params={"trainer_id": 1491 })
    assert response.status_code == 200

def test_trainer_name():
    response = requests.get(f'{host}/trainers', params={"trainer_id": 1491 })
    assert response.json()["trainer_name"] == "LamaRk"