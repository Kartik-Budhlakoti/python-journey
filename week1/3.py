spam =1
while spam <= 2:
    print('HI! I am using the while loop .')
    spam += 1


name = ''
while name != 'kartik':
    print('please type your name .')
    name = input('-->')
print('Thankyou')


while True:
    print('please type your name .')
    name = input('-->')
    if name == 'rishabh' :
        print('you dumb brat !')
        continue
    if name== 'kartik':
        break
print('Thankyou')


while True:
    print('Enter your name : ')
    name = input('-->')
    if name != 'kartik':
        print('Access Denied')
        continue
    print('Hello kartik . What is the password ? (Hint: it is a fish)')
    password = input('-->')
    if password == 'orcas':
        print('Access Granted')
        break
    else:
        print('Wrong password !')
print('Out of the loop ...')


name = ''
while not name:
    print('Enter your name : ')
    name = input('-->')
print('How many guests will you have ?')
num_of_guests= int(input('-->'))
if num_of_guests:
    print('Be sure to have enough room for all your guests.')
else:
    print('Ok, sorry for asking!')
print('Done')

#  --------------------------------------------------------------------------------------

import sys
print('Hello!')
for i in range(3):
    print('Anata wa genki desu ka , i is set to ' , i)
    # if i == 2:
        # sys.exit()
# continue instead of break will also give the same result
    print('Anata wa genki desu ka , i is set to ' + str(i))
print('Good bye!')


print('A mathematical question...')
sum = 0
print('Current sum is 0')
for i in range(0,101):
    sum += i
print('The final sum of integers from 0-100 is ' + str(sum))
print('Problem solved.')


sum=0
i=0
while True:
    sum = sum + i
    i = i+1
    if i == 101:
        print('thats all the numbers in range 0-100')
        break
print('the final answer is :', sum)


for i in range(5,-1,-1):
    if i == 3:
        continue
    print(i)


import random
for i in range(5):
    print(random.randint(1,10))


import random
secret_number = random.randint(1,30)
print('I am thinking of a number between 1 and 30.')
for guesses_taken in range(1,7):
    print('Take a guess.')
    guess = int(input('-->'))
    if guess < secret_number:
        print('OOPS! your guess is too low , AGAIN')
    elif guess > secret_number:
        print('OOPs! your guess is too high, AGAIN')
    else:
        break
if guess == secret_number:
    print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number was ' + str(secret_number))



import random , sys
print('ROCK ,PAPER, SCISSORS')

wins=0
losses=0
ties=0
while True:
    print('%s Wins, %s Losses, %s Ties ' %(wins, losses, ties))
    while True:
        print('Enter your move:(r)ock (p)aper (s)cissor or (q)uit')
        
        player_move = input('-->')
        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's' :
            break
        print('Type one of r,p,s or q.')
        print('The player has chosen ' , player_move, 'which is invalid.')

    if player_move == 'r':
        print('Rock versus ...')
    elif player_move == 'p':
        print('Paper versus ...')
    elif player_move=='s':
        print('Scissor versus ...')

    move_number = random.randint(1,3)
    if move_number == 1:
        computer_move = 'r'
        print('Rock')
    elif move_number == 2:
        computer_move = 'p'
        print('Paper')
    elif move_number==3:
        computer_move= 's'
        print('Scissors')

    if player_move == computer_move:
        print('It is a tie !')
        ties +=1
    elif player_move == 'r' and computer_move=='s':
        print('You win !')
        wins += 1
    elif player_move == 'p' and computer_move =='s':
        print('You lose !')
        losses +=1
    elif player_move == 's' and computer_move == 'p':
        print('You win !')
        wins += 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose !')
        losses += 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win !')
        wins += 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose !')
        losses += 1



