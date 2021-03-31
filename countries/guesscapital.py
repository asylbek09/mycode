#!/usr/bin/env python3
import json
import random

def getCapitals():

    capitals_json = open ('C:/Users/asylb/OneDrive/Documents/TLG/Python/mycode/countries/capitals.json', "r")

    capitals_dict = json.load(capitals_json)

    return capitals_dict

def prompt():
    client_prompt = input("To play the game enter <y> or <anything> to exit ")

    if client_prompt == 'y':
        findCapital(client_prompt)
    else:
        printThank()

def findCapital(client_prompt):
    capitals = getCapitals()
    randCountry = random.choice(capitals)
    country = randCountry['country']
    city = randCountry['capital']

    print(randCountry)
    while client_prompt:
            client_choice = input("What is the capital of: " + country + "? ")

            if client_choice.lower() == city.lower():
                print(f"Congratulations, {country}'s capital is {city}")
                try_again = input("Do you want to play again? Enter <y> to play or <anything> to exit ")
                if try_again == 'y':
                    findCapital(try_again)
                else:
                    printThank()
                break
            else:
                print("Try again please!")

def printThank():
    print("Thank you and have a great day!")

def main():
    prompt()

main()