def reverse_string(str):
    reversed_string = ''
    for i in range(len(str)-1, -1, -1):
        reversed_string += str[i]
    print(reversed_string)
reverse_string('The Homelander')

def is_palindrome(str1):
    reversed_string = ''
    for i in range(len(str1)-1, -1, -1):
        reversed_string += str1[i]
    if reversed_string == str1:
        return True
    else:
        return False
print(is_palindrome(input('Enter the string : ')))
import operator
def calc(op,num1,num2):
    ops = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
        '%' : operator.mod,
        '**' : operator.pow,
    }
    try:
        print(ops[op](num1,num2))
    except:
        print('Error : Invalid input(check for the divisor)')
calc('/',10, 0)

List1 = ['Ted' , 'maharaja', 'Wolf of Wallstreet']
print(List1[0], List1[-1])
List1.extend(['Blood diamond','Bahubali', 'KGF'])
List1.remove(List1[1])
print(List1)

sum=0
List2 = [1,2,3,4,5]
for i in List2:
    sum+= i
print(sum)
print(sum/len(List2))

value = input('What do you wanna check ?  --> ')
List3= ['aaaa','bbbb','cccc',1,True]
List3 = str(List3)
if value in List3:
    print('yes it is present')

List4 = [1,4,2,3,7,8,5,10]
even_list = []
for i in List4:
    if i%2==0:
        even_list.append(i)
print(even_list)

List1 = ['Ted' , 'maharaja', 'Wolf of Wallstreet']
List4 = [1,4,2,3,7,8,5,10]
combined = []
for i in List1:
    combined.append(i)
for j in List4:
    if j not in combined:
        combined.append(j)
print(combined)
