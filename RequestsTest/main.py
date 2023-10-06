import requests
token = "0b5b90debcebef2207b97642b5a01311"
host = 'https://api.pokemonbattle.me:9104'
response_new_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "yamaha", 
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"}, 
    headers = {"Content-Type":"application/json","trainer_token": token })
print(response_new_pokemon.text)

response_new_name_pokemon = requests.put(f'{host}/pokemons', json ={
    "pokemon_id": "11954",
    "name": "New yamaha",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"}, 
    headers={"Content-Type":"application/json","trainer_token": token })
print(response_new_name_pokemon.text)

response_pokeball = requests.post(f'{host}/trainers/add_pokeball', json={"pokemon_id": "11954"},  
    headers={"Content-Type":"application/json","trainer_token": token })
print(response_pokeball.text)
