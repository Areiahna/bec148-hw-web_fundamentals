import requests
import json


#TASK #1

# Write a Python script to make a GET request to the Pokémon API (https://pokeapi.co/api/v2/pokemon/pikachu).
# Extract and print the name and abilities of the Pokémon.
# Expected Outcome:
# The script should output the name of the Pokémon (Pikachu) and a list of its abilities.

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/snorlax")

if response.status_code == 200:
    poke_data = response.json()
    ability_count = len(poke_data["abilities"]) 
    index = 0

    poke_dict = {
        "name": poke_data["name"],
        "abilities" : []
    } 

    while index < ability_count :
        poke_dict["abilities"].append(poke_data["abilities"][index]["ability"]["name"])
        index += 1 
       
    print(poke_dict)

# Modify the script to fetch data for three different Pokémon.
# Create a function to calculate and return the average weight of these Pokémon.
# Print the names, abilities, and average weight of the three Pokémon.

print("=" * 50)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

def fetch_pokemon_data(alist):

    pokemons = []
    for pokemon in alist:

        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

        if response.status_code == 200:
            poke_data = response.json()
            ability_count = len(poke_data["abilities"]) 
            index = 0

            poke_dict = {
                    "name": poke_data["name"],
                    "abilities": [],
                    "weight": poke_data["weight"]
                }  
            
            while index < ability_count :
                poke_dict["abilities"].append(poke_data["abilities"][index]["ability"]["name"])
                index += 1 
            
            pokemons.append(poke_dict)
    return pokemons

print(fetch_pokemon_data(pokemon_names))