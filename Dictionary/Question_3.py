# This program uses a dictionary to keep a record of Dict_starships captains'

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
QUIT = 4

# main function
def main():
    # Create an empty dictionary.
    Dict_starships = {}

    # Initialize a variable for the user's choice.
    choice = 0

    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == LOOK_UP:
            look_up(Dict_starships)
        elif choice == ADD:
            add(Dict_starships)
        elif choice == CHANGE:
            change(Dict_starships)

# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('Captains and Starships')
    print('----------------------')
    print('1. Look up a Starship')
    print('2. Add a new Starship')
    print('3. Change a Starship')
    print('4. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

# The look_up function looks up a name in the
# Dict_starships dictionary.
def look_up(Dict_starships):
    # Get a name to look up.
    name = input('Enter the Captains name: ')

    # Look it up in the dictionary.
    print(Dict_starships.get(name, 'Captain Not found !.'))

# The add function adds a new entry into the
# Dict_starships dictionary.
def add(Dict_starships):
    # Get a name and Starship.
    name = input('Enter the Captains Name: ')
    Starship_Name = input('Enter a Starship name is is assign to: ')

    # If the name does not exist, add it.
    if name not in Dict_starships:
        Dict_starships[name] = Starship_Name
    else:
        print('That entry already exists.')

# The change function changes an existing
# entry in the Dict_starships dictionary.
def change(Dict_starships):
    # Get a name to look up.
    name = input('Enter the Captain name: ')

    if name in Dict_starships:
        # Get a new Starship.
        Starship_Name = input('Enter the new Starship assign: ')

        # Update the entry.
        Dict_starships[name] = Starship_Name
    else:
        print('That name is not found.')


# Call the main function.
main()




