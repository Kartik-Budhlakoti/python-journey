def hello ():
    print('Good Morning')
    print('Good Evening')
    print('Good Night')
hello()
hello()
print('one more time !')
hello()

def say_hello_to (name):
    print('Good Morning, ' + name)
    print('Good Evening, ' + name)
    print('Good night, ' + name )
say_hello_to('Kartik')
say_hello_to('Bob')
# print(name)

import random
def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'Ask again later'
    elif answer_number ==6:
        return 'Concentrate and ask again'
    elif answer_number == 7:
        return 'My reply is no'
    elif answer_number==8:
        return 'Outlook not so good'
    elif answer_number==9:
        return 'Very doubtful'
print('Ask a yes or no questions: ')
input('-->')
r = random.randint(1,9)
fortune = get_answer(r)
print(fortune)
# or print(get_answer(random.randint(1,9)))

import random
total_heads = 0
total_tails = 0
for i in range(100):
    if random.randint(0,1) == 0:
        print('H', end='')
        total_heads += 1
    else :
        print('T', end='')
        total_tails = total_tails +1
print()
print('Total number of Heads = ',total_heads , ', Total number of tails = ',total_tails)

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')
def b():
    print('b() starts')
    c()
    print('b() returns')
def c():
    print('c() starts')
    print('c() returns')
def d():
    print('d() starts')
    print('d() returns')
a()

eggs = 'sss'
def spam():
    eggs = 'sos'
    print(eggs)
spam()

def spam():
    eggs = 'spamspam'
    bacon()
    print(eggs)
def bacon():
    ham = 'hamham'
    eggs = 'baconbacon'
spam()

def spam():
    eggs = 'spam local'
    print(eggs)
def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)
eggs = 'global'
bacon()
print(eggs)

def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
print()
spam()
print(eggs)

# def spam():
#     global eggs
#     eggs = 'spam'
# def bacon():
#     eggs = 'bacon'
# def ham():
#     print(eggs)
# eggs = 'global'
# spam()
# print(eggs)

# def spam():
#     print(eggs)------- this line will cause error because python will not fall back for global variable eggs
#     eggs = 'spam local'
# eggs = 'global'
# spam()

def spam(divide_by):
    try:
        return 42/divide_by
    except:
        print('Error : Invalid argument.')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
print('')
def spam(divide_by):
    return 42/divide_by
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except:
    print('Error : Invalid argument.')

import time , sys
indent = 0
indent_increasing = True
try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)
        if indent_increasing:
            indent = indent +1
            if indent == 20:
                indent_increasing = False
        else:
            indent = indent -1
            if indent == 0:
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()

import time,sys
try:
    while True:
        for i in range(1,9):
            print('-' * (i*i))
            time.sleep(0.1)
        for i in range(7,1,-1):
            print('-' * (i*i))
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()

import random
def get_random_dice_roll():
    random_number = random.randint(1,6)
    return random_number
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())


user_input = int(input('Enter the integer : '))
def collatz(number):
    if (number)%2 == 0:
        divide = (number)//2
        return divide
        
    else :
        divide3 = 3*number+1
        return divide3
while user_input != 1 :
    print(user_input)
    user_input = collatz(user_input)
print(1)

