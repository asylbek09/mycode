import requests

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    groundctrl = requests.get(MAJORTOM)
    # groundctrl = requests.get(MAJORTOM).json()
    
    helmetson = groundctrl.json()
    print(helmetson)
    
    # this should say dict
    print(type(helmetson))

    print(helmetson["number"])

    # this returns a LIST of the people on this ISS
    print(helmetson["people"])

    # list the FIRST astro in the list
    print(helmetson["people"][0])

    # list the SECOND astro in the list
    print(helmetson["people"][1])

    # list the LAST astro in the list
    print(helmetson["people"][-1])

    # display every item in a list
    for astro in helmetson["people"]:
        # display what astro is
        print(astro)

    # display every item in a list
    for astro in helmetson["people"]:
        # display ONLY the name value associated with astro
        print(astro["name"])
    
if __name__ == "__main__":
    main()