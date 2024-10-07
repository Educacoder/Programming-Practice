num=0

while num<1:
    num=int(input('Enter a non-negative number: '))
    factorial=1

    for count in range(1,num+1):
        factorial=factorial*count
    print(f'Factorial of {num} is {factorial}')
