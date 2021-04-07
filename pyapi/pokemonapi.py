#!/usr/bin/env python3

# imports always go at the top of your code
import requests
import argparse

def main():
    pokeapi = "https://pokeapi.co/api/v2/pokemon/"
    
    pokemon = input("Which pokemon you want to see: ").lower()
    
    pokeapireq = requests.get(pokeapi + pokemon).json()
    
    front_default = pokeapireq['sprites']['front_default']

    print(f"Image url: {front_default}")
    
    game_indices = pokeapireq['game_indices']
        
    print(f"Number of game indices: {len(game_indices)}")

    for i in pokeapireq['moves']:
        moves = i['move']['name']
        print(f"{pokemon}'s moves: {moves}")
        
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--poke', help='Provide the name of Pokemon (or its PokeDex number)')
#     args = parser.parse_args()
main()