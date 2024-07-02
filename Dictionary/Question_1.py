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
print("Results for English", learnerResult[0])
print("Results for Math", learnerResult[1])
print("Results for Science", learnerResult[2])
print("==========================")

english_Mark = 0
math_Mark = 0
science_Mark = 0

for key in examResult:
    average = (examResult[key][0] + examResult[key][1] + examResult[key][2])/3
    print('Average marks of', key, ":%.2f" % average)

    english_Mark = english_Mark + examResult[key][0]
    math_Mark = math_Mark + examResult[key][1]
    science_Mark = science_Mark + examResult[key][2]

english_Mark = english_Mark / len(examResult)
math_Mark = math_Mark / len(examResult)
science_Mark = science_Mark / len(examResult)

print('===============================================')
print('Average results for English:%.2f' % english_Mark)
print('Average results for Math:%.2f' % math_Mark)
print('Average results for Science:%.2f' % science_Mark)
