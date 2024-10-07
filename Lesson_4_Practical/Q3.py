def display_menu():
    print("")
    print('Geometry calculator menu')
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Quit')
    print("")


def area_circle(radius):
# Implement the circle to accept a circle's radius as an
# argument and returns the area of the circle

def circle_circumference(…):
# Implement the circle function to accept a circle's radius as an
# argument and returns the circumference of the circle

def area_rectangle(….):
# Implement the rectangle functions to perform calculations related
# to accept a rectangle's width and length as arguments and returns
# the rectangle's area.

def perimeter_rectangle(…):
# Implement the perimeter function to accepts a rectangle's width
# & length as arguments and returns the rectangle's
# perimeter.

def main():
    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = 0
    while choice != 5:

        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice: '))

        # Implement the if-elif-else code below to perform the selected action.
        if choice == 1:
            radius = float(input("Enter the circle's radius: "))
            # print('The area of the circle = ….)
        elif choice == 2:
            #…
            #…
            #…
            #…
        elif choice == 5:
            print('Exiting the program. . .')
        else:
            print('Error: invalid selection.')

main()

