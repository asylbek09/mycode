#!/usr/bin/env python3

char_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz)")
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")

name = char_name.lower()
stat = char_stat.lower()

heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "he's a wizard",
    "archenemy": "Voldemort",},
"agent fitz":
    {"real name": "Leopold Fitz",
    "powers": "intelligence",
    "archenemy": "Hydra",}
}

print(f"{name.capitalize()}'s {stat.capitalize()} is: {heroes[name][stat]}")
#print(name.capitalize() + "'s " + stat.capitalize() + " is: " + heroes[name][stat])