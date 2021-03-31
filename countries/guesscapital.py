#!/usr/bin/env python3
import json
import random

def getCapitals():

    capitals_json = open ('C:/Users/asylb/OneDrive/Documents/TLG/Python/mycode/countries/capitals.json', "r")

    capitals_dict = json.load(capitals_json)

    return capitals_dict

def prompt():
    capitals = getCapitals()
    randCountry = random.choice(capitals)
    print(randCountry)

    client_choice = input("What is the capital of: " + randCountry['country'] + "? ")

    while client_choice:
        client_choice = input("What is the capital of: " + randCountry['country'] + "? ")

        if client_choice.lower() == randCountry['capital'].lower():
            print(f"Congratulations, {randCountry['country']}'s capital is {randCountry['capital']}")
            break
        else:
            print("Try again!")

def main():
    prompt()

main()