def box_print(symbol, width, height):
    if len(symbol)!=1:
        raise Exception('Symbol must be a single character string.')
    if width <=2 :
            raise Exception('Width must be greater then 2.')
    if height <=2 :
            raise Exception('Height must be greater than 2.')
    print(symbol*width)
    for i in range(height - 2 ):
        print(symbol + (' ' * (width-2))+symbol)
    print(symbol*width)
try:
    box_print('*' , 4,4)
    box_print('O', 10,5)
    box_print('zz' , 3,4)
    box_print('x',1,3)
except Exception as err:
     print('An exception has occured :' + str(err))
try:
    box_print('x',1,3)
except Exception as err:
     print('An exception has occured :' + str(err))

import logging
logging.basicConfig(level = logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
def factorial(n):
    logging.debug('Start of factorial(' +str(n) + ')')
    total = 1
    for i in range(1,n+1):
        total = total * i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial (' +str(n) + ')')
    return total
print(factorial(5))
logging.debug('End of program')

print('Enter the first number to add: ')
first = input('-->')
print('Enter the second number to add: ')
second = input('-->')
print('Enter the third number to add: ')
third = input('-->')
print('The sum is ' + first + second +third )

import random
heads = 0
for i in range(1,1001):
    if random.randint(0,1)==1:
        heads = heads+1
    if i == 500:
        print('Halfway done')
print('Heads came up ' + str(heads) + 'times.')

# spam=int(input('Enter the integer : '))
# assert spam>10

# eggs = 'hello'
# bacon = 'hello'
# assert eggs == bacon
# eggs = 'goodbye'
# bacon = 'GOODbye'
# assert eggs == bacon
# import logging 
# logging.basicConfig(level=logging.DEBUG , format =' %(asctime)s - %(levelname)s - %(message)s')

import random
result = ''
chance = 2
while chance >0:
    guess = ''
    while guess not in ('heads' , 'tails'):
        print('Guess the coin toss! Enter heads or tails :')
        guess = input('-->')
    toss = random.randint(0,1)
    if toss == 1:
        result = 'heads'
    else :
        result = 'tails'
    if result == guess:
        print('You got it!')
        break
    else:
        print('Nope!')
        chance = chance -1
        continue
if chance == 0:
    print('You are really bad at this game .')