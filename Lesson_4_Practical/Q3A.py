def display_menu():
    print("")
    print('Geometry calculator menu')
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Quit')
    print("")

# The area function accepts a circle's radius as an
# argument and returns the area of the circle.
def area_circle(radius):
    return 3.142 * radius**2

def circle_circumference(radius):
    return 3.142 * radius

# The rectangle has functions that perform
# calculations related to rectangles.
# The area function accepts a rectangle's width and
# length as arguments and returns the rectangle's area.
def area_rectangle(width, length):
    return width * length

# The perimeter function accepts a rectangle's width
# and length as arguments and returns the rectangle's
# perimeter.
def perimeter_rectangle(width, length):
    return 2 * (width + length)

def main():
# The choice variable controls the loop and
# holds the user's menu choice.
    choice = 0

    while choice != 5:
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice: '))

        # Perform the selected action.
        if choice == 1:
            radius = float(input("Enter the circle's radius: "))
            print(f'The area of the circle = {area_circle(radius):.2f}')
        elif choice == 2:
            radius = float(input("Enter the circle's radius: "))
            print(f'The circumference of the circle = {circle_circumference(radius):.2f}')
        elif choice == 3:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print(f'The area of rectangle = {area_rectangle(width,length):.2f}')
        elif choice == 4:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print(f'The perimeter of rectangle = {perimeter_rectangle(width, length):.2f}')
        elif choice == 5:
            print('Exiting the program. . .')
        else:
            print('Error: invalid selection.')

main()