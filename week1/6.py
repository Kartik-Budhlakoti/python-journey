print('Enter the name of your 1st cat : ')
cat_name_1 = input('-->')
print('Enter the name of your 2nd cat : ')
cat_name_2 = input('-->')
print('Enter the name of your 3rd cat : ')
cat_name_3 = input('-->')
print('Enter the name of your 4th cat : ')
cat_name_4 = input('-->')
print('The cats names are : ')
print(cat_name_1 + ' '+cat_name_2 +' '+cat_name_3 +' ' +\
     cat_name_4)

cat_names = []
while True :
    print('Enter the name of the cat ' + str(len(cat_names))+ ' (Or enter nothing to stop.) : ')
    name =input('-->')
    if name=='':
        break
    cat_names = cat_names + [name]
print('The cates names are : ')
for name in cat_names:
    print('  ' + name)

my_pets = ['Zophie' , 'Pooka', 'Fat-tail']
print('Enter a pet name: ')
name = input('-->')
if name not in my_pets:
    print('I do not have a pet named ' + name)
else :
    print(name + ' is my pet.')

spam = ['cat' , 'dog']
if spam[0] == 'cat':
    print('A cat is the first item .')
else:
    print('The first item is not a cat .')

spam = []
if len(spam) > 0 and spam[0] == 'cat':
    print('A cat is the first item on the list.')
else:
    print('The first item is not a cat.')

import random
messages =['It is certain',
           'It is decidedly so',
           'Yes definitely',
           'Reply hazy try again',
           'Ask again later',
           'Concentrate and ask again',
           'My replt is no',
           'Outlook not so good',
           'Very doubtful']
print('Ask a yes or no question :')
input('-->')
print(messages[random.randint(0,len(messages) -1)])

def eggs(some_parameter):
    some_parameter.append('Hello')
spam = [1,2,3]
eggs(spam)
print(spam)

#  Matrixscreensaver
# import random ,sys, time
# WIDTH =70
# try:
#     columns = [0] *WIDTH
#     while True:
#         for i in range(WIDTH):
#             if random.random()<0.02:
#                 columns[i]= random.randint(4,14)
#             if columns[i] ==0:
#                 print(' ', end='')
#             else:
#                 print(random.choice([0,1]), end='')
#                 columns[i]-=1
#         print()
#         time.sleep(0.1)
# except KeyboardInterrupt:
#     sys.exit()
