import re
# str = re.compile(r'91-\d{10}')
# print(str.search('91-8439345728'))
# print(str.search('415-555-4242'))
# print(str.search('81-8438795728'))

# str2 = re.compile(r'\w{4}')
# print(str2.findall('This is a very long test string with some words like good and code.'))

# str3 = re.compile(r'\w{6}\w*')
# print(str3.sub('******', 'Hi my name is kartik budhlakoti'))

# str4 = re.compile(r'python' , re.I)
# print(str4.findall('Hi i am following a python course and ' \
# 'i think PYTHON is quite interesting , like actual ' \
# 'PYthon eats slowly i started to like this slowly. '))

# list1 = ['kartikbudhlako@gmail.com ', 'kartikbudako@gmail@.in ',
# 'kartikbudhlako@gmail.org ',
# 'kartikbudhlako@gmail.org ','kartikbhlako@gmail',
# 'kartikbudhlako@gmail.com ','kartikbudhko@ ',
# 'kartikbudhlako@gmail.in ',
# 'kartikbudhlako@gmail.in ','kartikbudako@@gmail.com ']
# list2 = []
# list3 = []
# mail = re.compile(r'^\w+@\w+\.(org|in|com|net)$')
# for i in list1:
#     if mail.search(i.strip()):
#         list2.append(i.strip())
#     else:
#         list3.append(i.strip()) 
# print(list2)
# print()
# print(list3)

# str6 = '''
# 2024-03-15 INFO User logged in from 192.168.1.10
# 2024-03-15 ERROR Failed login from 10.0.0.5
# 2024-03-16 WARNING High memory usage on 172.16.0.1
# 2024-03-16 ERROR Database timeout from 192.168.1.105
# '''
# IPs = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
# Dates = re.compile(r'\d{4}-\d{2}-\d{2}')
# messages = re.compile(r'ERROR (.+)')
# print(IPs.findall(str6))
# print(Dates.findall(str6))
# print(messages.findall(str6))


# uppercase = re.compile(r'[A-Z]')
# lowercase = re.compile(r'[a-z]')
# digit = re.compile(r'[0-9]')
# special = re.compile(r'[!@#$%^&*]+')
# for i in range(5):
#     password = input('At least of length 8 : ')
#     if len(password)<8:
#         print('Small length than 8 , Again')
#         continue
#     if len(password)>=8:
#         if not uppercase.search(password):
#             print('No uppercase letter , AGAIN')
#             continue
#         if not lowercase.search(password):
#             print('no lowercase letter , AGAIN')
#             continue
#         if not digit.search(password):
#             print('no digit , AGAIN')
#             continue
#         if not special.search(password):
#             print('no special character , AGAIN')
#             continue
#     print('The password is Strong')

regex_pattern = re.compile(r'''
                            [0-3][0-9]-#date
                           [0-1][0-9]''',re.VERBOSE)#month
date = regex_pattern.search('Date is 22-12-1002')
print(date.group())