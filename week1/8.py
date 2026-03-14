# print('''Dear Alice,
      
#       Can you feed Eve's cat this weekend?
      
#       Sincerely,
#       Bob''')
# print('Dear Alice,\n\n      Can you feed Eve\'s cat this weekend?\n\n      ' \
# 'Sincerely,\n      Bob')

# '''This is a python program.

# Written by me to check the syntax '''
# def say_hello():
#     '''This function
#     prints hello'''
#     print('hello!')

while True:
    print('Enter your age : ')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
while True:
    print('Select a new password (letters and numbers only):')
    password= input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')