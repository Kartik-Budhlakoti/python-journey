# name = input('Enter Your name : ')
# age = int(input('Enter your age : '))
# college_name = input('Enter your college name : ')
# print(f'Hello {name} you are {age} years young and your College name is {college_name} ')

# num1 = float(input('Enter your number 1 : '))
# num2 = float(input('Enter your number 2 : '))
# print('The sum of two numbers is ', num1+num2)

# print(type(name))
# print(type(age))
# print(type(num1))

# temp = float(input('Enter the temperature in Celcius : '))
# Fahrenheit = (temp * (9/5))+ 32
# print('The temperature in fahrenheit is : '+ str(Fahrenheit))

# age = int(input('How old are you  : '))
# days = age * 365
# hours = days * 24
# minutes= hours * 60
# print('So basically you are ' + str(days) + ' Days old.')
# print('Or you basically you are ' + str(hours) + ' hours old.')
# print('Or ' + str(minutes) + ' minutes old.')

# a= 16
# b= 19
# print(a,b)
# a,b = b,a 
# print(a,b)

# bill_amt = float(input('Enter the amount in $ : '))
# tip_percent = float(input('Enter the tip percentage : '))
# tip_amt = bill_amt* tip_percent
# total_bill = bill_amt + tip_amt
# each_person_bill = bill_amt/4
# print(f'   So the bill amount was : ${bill_amt:2f}') 
# print(f'    And the tip of : {tip_percent}%')
# print(f'   The Total amount is :  ${total_bill:2f}')
# print(f'    After splitting 4 ways the amount is ${each_person_bill:2f} each.')

# num = float(input('Enter the number : '))
# if num<0:
#     print('The number is negative.')
# elif num== 0:
#     print('The number is 0.')
# else:
#     print('The number is positive.')

# for i in range(51):
#     print(i)

# i=0
# while True:
#     num = int(input('Enter the number : '))
#     if num ==0:
#         break
#     else:
#         i+=1     
# print(i-1)

# num = int(input('Enter the number for its multiplication table : '))
# mul = 0
# for i in range(1, 11):
#     mul = num * i
#     print(num ,' * ', i,' = ',  mul)

# for i in range (1,101):
#     if i%3==0 and i%5==0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i) 
        

while True:
    user_name = input('Enter the username of ' \
    'atleast 6 characters with no space in between : ')
    if len(user_name) < 6:
        print('oops less than 6 characters.')
        continue
    elif ' ' in user_name:
        print('opps the name contains space.')
        continue
    else:
        break
