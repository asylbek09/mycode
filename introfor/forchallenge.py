farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

print("CHALLENGE 1")
print(farms[0]["agriculture"])

for animal in farms[0]["agriculture"]:
    print(animal)

print("\nCHALLENGE 2")

choice = input("Choose farm: NE Farm, W Farm, or SE Farm ")

for eachdict in farms:
    if choice in eachdict["name"]:
        # print(eachdict["agriculture"])
        for agitem in eachdict["agriculture"]:
            print(agitem)

print("\nCHALLENGE 3")

choice = input("Choose farm: NE Farm, W Farm, or SE Farm ")
yuck = ["carrot", "celery"]

for eachdict in farms:
    if choice in eachdict["name"]:
        # print(eachdict["agriculture"])
        for agitem in eachdict["agriculture"]:
            if agitem not in yuck:
                print(agitem)

noveggies = []

for agitem in farms[2]["agriculture"]:
    if agitem not in ["carrots", "celery"]:
        noveggies.append(agitem)

print(noveggies)

# list comprehension
noveggies2 = [agitem for agitem in farms[2]["agriculture"] if agitem not in ["carrots", "celery"]]
print(noveggies2)