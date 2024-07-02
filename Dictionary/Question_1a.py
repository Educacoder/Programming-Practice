#1a Create a examResult to store the above data. Use list[] enclosed by disctionary{}
examResult = {'Jane': [75, 80, 85],
              'John':[60, 68, 74],
              'Jerome':[81, 63, 77],
              'Jason':[55, 76, 67],
              'Jessica':[62, 45, 68],
              'Joanne':[52, 47, 51]}
#How user to query the result

stud_name = input('Enter learner name to query: ')

#Use dict.get(key,value)

learnerResult = examResult.get(stud_name, 'learner does not exist!')
print("Results of", stud_name)
print("==========================")
print("Results for English",examResult[stud_name][0])
print("Results for Math", learnerResult[1])
print("Results for Science", learnerResult[2])
print("==========================")
