import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'сюда вставляешь свой токен'
HEADER = {'Content-Type':'application/json' , 'trainer_token':TOKEN}
body_creat = {
    "name": "generate",
    "photo_id": -1
}
body_change = {
    "pokemon_id": "44555",
    "name": "MrPickles"
}
body_catch = {
    "pokemon_id": "44555"
}

'''response_creat = requests.post(url = f'{URL}/v2/pokemons' , headers = HEADER , json = body_creat)
print(response_creat.text)'''

'''response_change = requests.patch(url = f'{URL}/v2/pokemons' , headers = HEADER , json = body_change)
print(response_change.text)'''

response_catch = requests.post(url = f'{URL}/v2/trainers/add_pokeball' , headers = HEADER , json = body_catch)
print(response_catch.text)

