from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#
player.location is room['foyer']
# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
starting_room = Player(room['outside'])
current_room = Player(room['outside'])
outside = Player(room['outside'])
overlook_room = Player(room['overlook'])
foyer_room = Player(room['foyer'])
treasure_room = Player(room['treasure'])
narrow_room = Player(room['narrow'])
# Write a loop that:
while True:
   # Prints the current room name
    print(player.location)
    command = input("> ").split(',')

    if command[0] == 'q':
        break
            
    elif command[0] == 'n':
        if current_room == foyer_room:
            overlook_room = Player(room['overlook'])
            print(overlook_room.location)
        elif current_room == outside:
            foyer_room = Player(room['foyer'])
            print(foyer_room.location)
        elif current_room == treasure_room:
            print('You can only go south')
        elif current_room == narrow_room:
            treasure_room = Player(room['treasure'])
            print(treasure_room.location)
    elif command[0] == 's':
        outside_room = Player(room['outside'])
        if starting_room == outside_room:
            print('You can only move north')
            outside_room = Player(room['outside'])
        elif current_room == foyer_room:
            current_room = Player(room['outside'])
            print(current_room.location)

    # elif command[0] == 'e':

    # elif command[0] == 'w':

# * 
    
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
