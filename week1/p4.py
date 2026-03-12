list = [1,2,3,4,5]
positions = 2
front = list[:positions]
for i in range(len(list) - positions):
    list[i]= list[i+positions]
    print(list)
for i in range(positions):
    list[len(list)-positions +i] = front[i]
    print(list)
print(list)

list1 = list[0:positions]
list2 = list[positions:(len(list))]
list = list2+list1
print(list)

def func(list,sum):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == sum:
                return [list[i], list[j]]
    return None
list =  [2,7,11,15] 
print(func(list,sum = 9))

dict1= {'name':'kartik', 'age':'20','college' : 'BIAS', 'year':2026 ,'favorite_lang': 'urdu'}
for k,v in dict1.items():
    print('Key: ' ,k, '    Value: '+str(v))
key=input('enter the key : ')
value=input('enter the value : ')
dict1[key]=value
print(dict1)
dict1.pop('name')
print(dict1)
dict1.popitem()
print(dict1)
dict1.update({'age':'21'})
print(dict1)

import sys
while True:
    checker = input(' key --> ')
    if checker.lower()=='quit':
        break
    if checker in dict1:
        print('yes its present and its value is : ',dict1[checker])
    else:
        value= input('Now enter its value : ')
        dict1[checker] = value
        print('Updated dict : ', dict1)
        sys.exit()


