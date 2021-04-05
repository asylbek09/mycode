#!/usr/bin/python3
import random
import sys
from data import *
# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
Welcome to Chicago, Save the city from villains!
===================================================
Commands:
  go [north, south, east, west]
  get [pistol, knife, armor, rifle, helmet, yogurt]
  q [to quit the game]
''')

def showStatus():
    #print the player's current status
    print('---------------------------------')
    print('You are in the ' + currentcity)
    print(f"You are {player} your health: {my_health} and damage: {my_power}")
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in city[currentcity]:
        print('You see a ' + city[currentcity]['item'])
    print('---------------------------------')

def randomEnemy(currentcity, my_health, my_power):
    # assigning random enemy if rand int equals city's 0
    if random.randint(0, 1) == city[currentcity]['villain']:
        rand_enemy = random.choice(list(enemy))
        print(f'''You just encountered villain {rand_enemy} in {currentcity}''')
        print("Kill it and save the city!!!")
        combat(rand_enemy, my_health, my_power)

def combat(rand_enemy, my_health, my_power):
    enemy_health = enemy[rand_enemy]['health']
    enemy_power = enemy[rand_enemy]['damage']
    
    while True:
        
        if enemy_health <= 0 and enemy_health < my_health:
            print(f"Congratulations you killed {rand_enemy} and saved the city from villains")
            sys.exit()
        elif my_health <= 0:
            print(f"GAME OVER, {rand_enemy} killed you!")
            sys.exit()
        
        print(f"Fighting {rand_enemy}")
        print(f"Your health: {my_health}, damage: {my_power}, inventory: {inventory}")
        print(f"{rand_enemy}'s health: {enemy_health} and damage: {enemy_power}")
        
        action = input('''Enter <p> to use your power
<a> to use armory
<h> to increase health
---------------------------------
>''')
        
        if action.lower() == 'p':
            enemy_health -= my_power
            my_health -= enemy_power
        elif action.lower() == 'a' and len(inventory) != 0:
            weapon = input(f"Select armory to fight from inventory: {inventory} ")
            if weapon in inventory:
                my_health -= enemy_power
                enemy_health -= armory[weapon]['damage']
                inventory.remove(weapon)
        elif action.lower() == 'h' and len(inventory) != 0:
            # health increased if helmet, armor or yogurt gets picked up
            strength = input(f"Select item to boost health: {inventory} ")
            if strength in inventory:
                my_health += life[strength]['health']
                inventory.remove(strength)
        elif action.lower() == 'q':
            break

def playGame(): 
    
    global inventory, currentcity, player, my_health, my_power
    
    #an inventory, which is initially empty
    inventory = []

    showInstructions()
    
    # player can select a hero or get randomly assigned one
    selection = input('''Enter X-Man <name> or <r> to get assigned randomly:
Professor X, Beast, Wolverine, Cyclops, Phoenix
---------------------------------
>''').title()
    while selection not in xmen and selection != 'R':
        selection = input("Please enter <name> or <r>! ").title()
    if selection == 'R':
        player = random.choice(list(xmen))
    else:
        player = selection
        
    my_health = xmen[player]['health']
    my_power = xmen[player]['damage']
    
    print('---------------------------------')
    print(f"You selected: {player}")
    print(f"{player}'s health: {xmen[player]['health']} and damage: {xmen[player]['damage']}")
    print('---------------------------------')
    
    #start the player in the chosen city
    selectCity = input('''Where do you want to start your adventure?
Enter city <name> or <r> to start from random place: 
Downtown, River North, Old Town, Streeterville, River West
United Center, Greektown, Grant Park, Lake Michigan, 
Pilsen, South Loop, Field Museum, Chinatown
---------------------------------
>''').title()
        
    while selectCity not in city and selectCity != 'R':
        selectCity = input("Please enter <name> or <r>! ").title()
    if selectCity == 'R':
        currentcity = random.choice(list(city))
    else:
        currentcity = selectCity
        
    #loop forever
    while True:
        showStatus()

        #get the player's next 'move'
        #.split() breaks it up into an list array
        #eg typing 'go east' would give the list:
        #['go','east']
        move = ''
        while move == '':
            move = input('>')

        # split allows an items to have a space on them
        # get golden key is returned ["get", "golden key"]          
        move = move.lower().split(" ", 1)

        #if they type 'go' first
        if move[0] == 'go':
            #check that they are allowed wherever they want to go
            if move[1] in city[currentcity]:
                #set the current room to the new room
                currentcity = city[currentcity][move[1]]
                # setting random enemy in the city and calling combat func
                randomEnemy(currentcity, my_health, my_power)
            else:
                print('You can\'t go that way!')

        #if they type 'get' first
        if move[0] == 'get' :
            #if the room contains an item, and the item is the one they want to get
            if "item" in city[currentcity] and move[1] in city[currentcity]['item']:
                #add the item to their inventory
                inventory += [move[1]]
                #display a helpful message
                print(f"You just picked up {move[1]}!")
                #delete the item from the room
                del city[currentcity]['item']
            #otherwise, if the item isn't there to get
            else:
                #tell them they can't get it
                print('Can\'t get ' + move[1] + '!')
        
        if move[0] == 'q':
            break
            
        ## Define how a player can win
        if currentcity == 'Pilsen' and 'time gem' in inventory and 'power gem' in inventory:
            print('You Collected the infinite stones which will save the world... YOU WIN!')
            break

        ## If a player enters a room with a monster
        elif 'item' in city[currentcity] and 'venom' in city[currentcity]['item']:
            print('A venom has got you... GAME OVER!')
            break
    
def main():
    playGame()
    
main()