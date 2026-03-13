students = {
    'kartik' : [75 , 82,90],
    'amit' : [60,55,79],
    'priya': [88,92,40]
}

for v in students.values():
    sum = 0
    for i in v:
        sum = sum + i
    avg= sum/len(v)
    print(avg)

students = {
    'student1':{'name':'Kartik', 'subjects':['OS','CN','AI']},
    'student2':{'name':'Amit', 'subjects':['Maths', 'Physics']},
    'student3':{'name':'priya','subjects':['OS','AI','OE','IoT']}
}
for v in students.values():
    for key,values in v.items():
        if key == 'subjects':
            subjects = len(values)
            print(subjects)

dict1 = {'name' : 'kartik', 'age' : 20 , 'learning':'python'}
dict2 = {'name':'mohit' , 'status':'single', 'health':'good'}
dict3 = {}
for k,v in dict1.items():
    dict3[k] = v
for k,v in dict2.items():
    dict3[k] = v
print(dict3)

students = {
    "Kartik": 65,
    "Amit": 63,
    "Priya": 55,
    'Rava': 35,
    'Adam': 71
}
for k,v in students.items():
    if v>60:
        print(k ,' scored ',v, ' marks which are above 60')

dict ={'India':'Delhi','Iran':'Tehran',
        'China':'Beijing','Japan':'Tokyo' }
while True:
    user_input = input('Enter the country (or enter quit to stop) : ')
    if user_input.lower()=='quit':
        break
    found = False
    for k in dict.keys():
            if user_input.lower() == k.lower():
                print('Capital : ',dict[k])
                found = True
                break
    if not found:
        print('Not found')

products = {'apples':4 , 'bananas':12, 'eggs':30, 'onions':3}
num = {}
for k,v in products.items():
    if v>5:
        num[k]=v
print(products)
print(num)

dict3 = {}
for i in range (1,6):
    key = input(f'enter the key {i} : ')
    value = input(f'enter the value for key{i} : ')
    dict3[key]=value
print(dict3)