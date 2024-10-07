student = int(input("How many students do you have? "))
test = int(input("How many test for your module? "))

for num in range(student):
    total = 0.0
    print(f"******* Student #{num+1} *******")

    for count in range(test):
        score = float(input(f"Test number {count+1}: "))
        total += score
        average = total / test
        print(f"The average for student #{num+1} is: {average}\n")