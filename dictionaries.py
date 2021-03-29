#!/usr/bin/env python3

char_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz or -1 to EXIT)")
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")

heroes = {
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

while char_name != -1:
    name = char_name.lower()
    stat = char_stat.lower()

    print(name.capitalize() + "'s " + stat.capitalize() + " is: " + heroes[name][stat])
     continue

