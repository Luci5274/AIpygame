#define the rooms
rooms = {
    'hallway': {
        'description': 'You are in a dimly lit hallway.',
        'exits': {'north': 'kitchen', 'east': 'living room'}
    },
    'kitchen': {
        'description': 'You are in a messy kitchen.',
        'exits': {'south': 'hallway'}
    },
    'living room': {
        'description': 'You are in a cozy living room.',
        'exits': {'west': 'hallway'}
    }
}

# Initialize player position
current_room = 'hallway'

# Initialize AI position
ai_position = 'living room'

# Function to move the player
def move(direction):
    global current_room
    if direction in rooms[current_room]['exits']:
        current_room = rooms[current_room]['exits'][direction]
        print(rooms[current_room]['description'])
    else:
        print("You can't go that way!")

# Function to move the AI
def ai_move():
    global ai_position
    # In this simple example, the AI character always moves randomly
    directions = list(rooms[ai_position]['exits'].keys())
    direction = random.choice(directions)
    ai_position = rooms[ai_position]['exits'][direction]
    
    # Game loop
while True:
    print(rooms[current_room]['description'])

    command = input("What do you want to do? (Type 'help' for instructions): ").lower()

    if command == 'help':
        print("Available commands: move [direction], quit")
    elif command.startswith('move'):
        direction = command.split()[1]
        move(direction)
        ai_move()
        if current_room == ai_position:
            print("Oh no! The AI caught you!")
            break
    elif command == 'quit':
        print("Thanks for playing!")
        break
    else:
        print("Invalid command. Type 'help' for instructions.")
        
        # Start the game
if __name__ == "__main__":
    import random
    main()