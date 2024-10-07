examResult = {'Jane':[75,80,85],
              'John':[60,68,74],
              'Jerome':[81,63,77],
              'Jason':[55,76,67],
              'Jessica':[62,45,68],
              'Joanne':[52,47,51]}
englishMark = 0
mathMark = 0
scienceMark = 0

print(examResult['Jane'][0])
# print(examResult['Jane'][1])
# print(examResult['Jane'][2])
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


for key in examResult:
    average = (examResult[key][0] + examResult[key][1] + examResult[key][2])/len(examResult[key])
    print("Average marks of", key, ":%.2f" % average)

    englishMark += examResult[key][0]
    mathMark += examResult[key][1]
    scienceMark += examResult[key][2]

english_ave = englishMark/len(examResult)
math_ave = mathMark/len(examResult)
science_ave = scienceMark/len(examResult)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print('Average results for English:%.2f' %english_ave)
print('Average results for Math:%.2f' %math_ave)
print('Average results for Science:%.2f' %science_ave)
