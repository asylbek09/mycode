#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        print(f"\nNAME: {gotresp['name']}")
        print("\nHOUSE(S):")
        for family in gotresp["allegiances"]:
            familyresp= requests.get(family).json()
            print(familyresp["name"])
        print("\nBOOK(S):")
        for book in gotresp["books"]:
            bookresp= requests.get(book).json()
            print(bookresp["name"])
        for book in gotresp["povBooks"]:
            bookresp= requests.get(book).json()
            print(bookresp["name"])

if __name__ == "__main__":
        main()
