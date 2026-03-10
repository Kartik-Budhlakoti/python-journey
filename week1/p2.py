for i in range(6):
    print('*'* i)
    
max_attempt_username=3
password_attempt = 3
x=1
while x>0:
    if max_attempt_username>0:
        user_name = input('Enter the username : ')
        if user_name != 'kartik':
            max_attempt_username -=1
            print('Wrong username ','---Attempts left = ',max_attempt_username )
            continue
        else:
            print('Welcome kartik! whats the password ?')
    else :
        print('Authentication Failed')
        break
    while password_attempt>0:
        password = input('Enter the password to verify : ')
        if password!= 'budhlakoti':
            password_attempt -= 1
            print('Wrong password ---------Attempts left = ', password_attempt)
            continue
        else:
            x -= 1
            print('Hey it really is you BOSS')
            break    

import sys
num = int(input('Enter the number you want to check : '))
if num<=1:
    print('Not prime(must be > 1)')
    sys.exit()
is_prime = True
for i in range(2,int(num**0.5) +1):
    if num % i ==0:
        print('The number is not prime since it is divisible by : ', i)
        is_prime = False
        break
if is_prime:
    print('The number is prime.')

def greet(name):
    print(f'Hello {name} welcome!')
greet(name= input('Enter your name : '))

def is_even(num):
    if num%2 == 0:
       return True
    else :
        return False
print(is_even(num=int(input('Enter the number you want to check : '))))

def count_vowels(str):
    count =0
    vowels_str = 'aeiouAEIOU'
    for char in str:
        if char in str:
            if char in vowels_str:
                count += 1
    return count
print(count_vowels(str = input('Enter the string : ')))