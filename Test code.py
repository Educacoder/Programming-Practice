# Q3- Using not in for User input only(A, B, C and D)
# answer using list
# student input in empty list
answerList = ['C','D','B','A','B','D','A','C','D','C']
mark = 0
MCQ_in= ['A','B','C','D']

while True:
    studentAttempt = []
    print('Please enter your Review Exercise answer')
    for n in range(10):
        # modulus operator % input
        student_data = input("Enter MCQ #%d: " %(n+1))
        while student_data not in MCQ_in:
            student_data = input("Please enter again MCQ #%d: " % (n+1))

        studentAttempt.append(student_data)

    count = 0
    for i in range(10):
        if answerList[i] == studentAttempt[i]:
            count = count+1
    mark = count
    print('You have %d correct answer and %d wrong answer' %(mark, 10-mark))

    tryAgain = input("Do you want to try again? (Y/N)")

    if tryAgain == 'Y' or tryAgain =='y':
        studentAttempt = []
        continue
    else:
        break
print(f'Your mark for Review Exercise is {mark:.2f}')
print(f'The correct exercise answers:')
print(answerList)