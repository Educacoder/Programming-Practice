#1a Create a examResult to store the above data. Use list[] enclosed by dictionary{}

examResult = {'Jane':[75,80,85],
              'John':[60,68,74],
              'Jerome':[81,63,77],
              'Jason':[55,76,67],
              'Jessica':[62,45,68],
              'Joanne':[52,47,51]}

name = input('Enter student name ')
studentResult = examResult.get(name,['Student does not exist!','Student does not exist!','Student does not exist!'] )
average = (studentResult[0] + studentResult[1] + studentResult[2] ) / 3

print("Result of", name)
print("###################")
print('English:', studentResult[0])
print('Math:', studentResult[1])
print('Science:', studentResult[2])
print('Average marks of', name , ":%.2f" %average)
