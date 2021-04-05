#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
city = {
            'Downtown'    : {
                  'north' : 'River North',
                  'south' : 'South Loop',
                  'east'  : 'Grant Park',
                  'west'  : 'Greektown',
                  'item'  : 'knife',
                  'villain' : 0
                },
            # Downtown to the North
            'River North' : {
                  'north' : 'Old Town',
                  'south' : 'Downtown',
                  'east'  : 'Streeterville',
                  'west'  : 'River West',
                  'item'  : 'pistol',
                  'villain' : 0
                },
            # Downtown to the South
            'South Loop'  : {
                  'north' : 'Downtown',
                  'south' : 'Chinatown',
                  'east'  : 'Field Museum',
                  'west'  : 'Pilsen',
                  'item'  : 'rifle',
                  'villain' : 0
               },
            # Downtown to the East
            'Grant Park' : {
                  'north' : 'Streeterville',
                  'south' : 'Field Museum',
                  'east'  : 'Lake Michigan',
                  'west'  : 'Downtown',
                  'item'  : 'Armor',
                  'villain' : 0
               },
            # Downtown to the West
            'Greektown'   : {
                  'north' : 'River West',
                  'south' : 'Pilsen',
                  'east'  : 'Downtown',
                  'west'  : 'United Center',
                  'item'  : 'greek yogurt',
                  'villain' : 0
            },
            # Old Town
            'Old Town'    : {
                  'south' : 'River North',
                  'item'  : 'helmet',
                  'villain' : 0
            },
            # Streeterville
            'Streeterville' : {
                  'west'  : 'River North',
                  'south' : 'Grant Park',
                  'item'  : 'pistol',
                  'villain' : 0
            },
            # River West
            'River West' : {
                  'east' : 'River North',
                  'south' : 'Greektown',
                  'item' : 'knife',
                  'villain' : 0
            },
            # Chinatown
            'Chinatown' : {
                  'north' : 'South Loop',
                  'item'  : 'venom',
                  'villain' : 0
            },
            # Field Museum
            'Field Museum' : {
                  'north' : 'Grant Park',
                  'west'  : 'South Loop',
                  'item'  : 'rifle',
                  'villain' : 0
            },
            # Lake Michigan 
            'Lake Michigan' : {
                  'west' : 'Grant Park',
                  'item' : 'time gem',
                  'villain' : 0
            },
            # Pilsen
            'Pilsen' : {
                  'north' : 'Greektown',
                  'east'  : 'South Loop',
                  'item'  : 'power gem',
                  'villain' : 0
            },
            # United Center
            'United Center' : {
                  'east' : 'Greektown',
                  'item' : 'knife',
                  'villain' : 0
            }
         }

enemy = {
      'Magneto' : { 'health' : 20, 'damage' : 10 },
      'Apocalypse' : { 'health' : 17, 'damage' : 8 },
      'Mystique' : { 'health' : 10, 'damage' : 5 },
      'Sabretooth' : { 'health' : 14, 'damage' : 7 },
      'Juggernaut' : { 'health' : 11, 'damage' : 6 }
}

xmen = {
      'Professor X' : { 'health' : 20, 'damage' : 10 },
      'Beast' : { 'health' : 17, 'damage' : 6 },
      'Wolverine' : { 'health' : 18, 'damage' : 9 },
      'Cyclops' : { 'health' : 15, 'damage' : 7 },
      'Phoenix' : { 'health' : 19, 'damage' : 9 }
}

armory = {
      'knife' : { 'damage' : 4 },
      'pistol' : { 'damage' : 5 },
      'rifle' : { 'damage' : 6 },
      'venom' : { 'damage' : 8 }
}

life = {
      'helmet' : { 'health' : 2 },
      'armor' : { 'health' : 3 },
      'greek yogurt' : { 'health' : 10 }
}