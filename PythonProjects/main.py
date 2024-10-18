import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c25aedc9ef1ca7d0862dd14969b3a27f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_registration = {
    "name": "generate",
    "photo_id": -1
}

body_change_name = {
    "pokemon_id": "98537",
    "name": "Пштоgun",
    "photo_id": 54
}

body_pokeball = {
    "pokemon_id": "98537"
}



'''response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_registration)
print(response.text)

responce_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(responce_change_name.text) '''

reponse_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(reponse_pokeball.text)

pokemon_id = reponse_pokeball.json()['id']
print(pokemon_id)
