print('''Dear Alice,
      
      Can you feed Eve's cat this weekend?
      
      Sincerely,
      Bob''')
print('Dear Alice,\n\n      Can you feed Eve\'s cat this weekend?\n\n      ' \
'Sincerely,\n      Bob')

'''This is a python program.

Written by me to check the syntax '''
def say_hello():
    '''This function
    prints hello'''
    print('hello!')

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

print('How are you? ')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

# import pyperclip
# text = pyperclip.paste()
# alt_text = ''
# make_uppercase = False
# for character in text:
#     if make_uppercase:
#         alt_text += character.upper()
#     else:
#         alt_text += character.lower()
#     make_uppercase = not make_uppercase
# pyperclip.copy(alt_text)
# print(alt_text)

print('Enter the English message to translate into pig latin:')
message=input()
VOWELS = ('a','e','i','o','u','y')
pig_latin = []
for word in message.split():
    prefix_non_letters = ''
    while len(word)>0 and not word[0].isalpha():
        prefix_non_letters +=word[0]
        word = word[1:]
    if len(word)==0:
        pig_latin.append(prefix_non_letters)
        continue

    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters= word[-1]+suffix_non_letters
        word = word[:1]
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()

    prefix_consonants =''
    while len(word)>0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'

    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()
    pig_latin.append(prefix_non_letters +word +suffix_non_letters)
print(' '.join(pig_latin))        
