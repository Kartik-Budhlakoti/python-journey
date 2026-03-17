str1 = input('Enter a sentence : ')
print(str1.lower())
print(str1.upper())
print(str1.title())

str2 = 'Hello, Testing this string for its ending and beginning.bye'
str3 = '2 This is the secong string to be tested.'
if str2.startswith('Hello'):
    print('The starting is good')
if str2.endswith('bye'):
    print('The ending is good')
if not str3.startswith('Hello'):
    print("Not starting with 'Hello'")
if not str3.endswith('bye'):
    print("Not ending with 'bye'")

str4 = ' This is the string used for strip method  '
print(len(str4))
str4 = str4.strip()
print(len(str4))

str5 = 'Hello my name is KARTIK'
str5 = str5.split(' ')
for i in str5:
    print(i)

str6 = input('Enter the string that is to be checked : ')
if str6.isalpha():
    print('The string is all alphabetic.')
elif str6.isdecimal():
    print('The string is all numeric.')
elif str6.isalnum():
    print('The string is mixed.')
else:
    print('Out of scope.')

str = input("Enter the string 'Race car' or 'A min a plan a canal Panama' : ")
str = str.lower().split()
str= "".join(str)
mid = len(str)//2
str1 = str[:mid]
str2 = str[-mid:]
str3 = str2[::-1]
if str1 == str3:
    print('The string is palindrome.')
else:
    print('NOt palindrome.')

s = ('Hey all I am kartik and i work also since i that is'
' kartik am a student, i am doing Student work so that is all')
s = s.lower().split()
ss = set(s)
word_count = {}
for i in ss:
    word_count[i]= s.count(i)
for word in sorted(word_count, key=word_count.get, reverse=True):
    print(word + ':', word_count[word])
print

def password_validator(password):
    if password.lower() == 'quit':
        return False
    if len(password)< 8:
        print('The password should be greater than or equal to 8 chars, re-enter : ')
        return False
    stripped = password.strip()
    if not any(c.isupper() for c in stripped ):
        print('At least 1 uppercase letter, re-enter : ')
        return False

    if not any(c.islower() for c in stripped ):
         print('At least 1 lowercase letter, re-enter : ')
         return False

    if not any(c.isdecimal() for c in stripped ):
        print('At least 1 digit, re-enter : ')
        return False

    if password != stripped:
        print('Spaces present, re-enter : ')
        return False

    print('The password is Strong')
    return True

password = input('Enter a strong password(or enter quit to end) : ')
password_validator(password)

print('Test_case 1...')
password_validator('weak')
print('Test_case 1...')
password_validator('AbcDefgh')
print('Test_case 1...')
password_validator('AbcDefg12')

sentence = "Hey ! I'm Kartik Budhlakoti"
while True:
    word = input('Enter the word to search for(or enter quit to exit ) : ')
    if word.lower() == 'quit':
        break
    else:
        if word in sentence:
            print(word ,' at ',sentence.find(word))
        else:
            print('Word not found.')

vowels = 'a','e','i','o','u'
strx = ('Hey all I am kartik and i work also since i that is'
' kartik am a student, i am doing Student work so that is all')
count = 0
for char in strx.lower():
    if char in vowels:
        count += 1
print(count)