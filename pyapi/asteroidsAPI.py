#!/usr/bin/python3
import requests
import pprint
import json

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("C:/Users/asylb/OneDrive/Documents/TLG/Python/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = "2020-09-09" #input("Enter start date in format: yyyy-mm-dd ")

    enddate = "2020-09-10" #input("Enter end date in format: yyyy-mm-dd ")
    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + "start_date=" + startdate + "&end_date=" + enddate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()
    #jsonData = json.dumps(neodata)
    #f = open("nasa,json", "w")
    #f.write(jsonData)
    #f.close()
    size= 0
    asteroid_distance= 0
    asteroid_names= []
    danger_count= 0

    print(f"Total Asteroids in Range: {neodata['element_count']}")
    for date in neodata["near_earth_objects"].keys():
        for aster in neodata["near_earth_objects"][date]:
            asteroid_names.append(aster["name"])
            if aster["estimated_diameter"]["kilometers"]["estimated_diameter_max"] > size:
                size= aster["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
            if float(aster["close_approach_data"][0]["miss_distance"]["lunar"]) > asteroid_distance:
                asteroid_distance = float(aster["close_approach_data"][0]["miss_distance"]["lunar"])
            if aster["is_potentially_hazardous_asteroid"]:
                danger_count += 1

    print(f"Largest Asteroid (kilometers): {size}")
    print(f"Closest Asteroid (lunar): {asteroid_distance}")
    print(f"Number of potentially hazardous asteroids: {danger_count}")
    input("Press ENTER to see a list of all asteroids.")
    print(set(asteroid_names))size = 0

    ## display NASAs NEOW data
    #print(neodata)
    #pprint.pprint(neodata)
    

if __name__ == "__main__":
    main()
