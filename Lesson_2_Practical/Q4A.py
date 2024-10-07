HIGH_SCORE = 95

# Enter the score for test 1, test 2 and test 3
test1 = int(input("Enter the score for test 1: "))
test2 = int(input("Enter the score for test 2: "))
test3 = int(input("Enter the score for test 3: "))

# Calculate the average score of the tests
average = (test1 + test2 + test3) / 3
# Print the average score
print(f"The average score is {average}")
# Check if the average score is greater or equal 95
if average >= HIGH_SCORE:
# Print "Congratulations! Good job!"
    print("Congratulations! Good job!")