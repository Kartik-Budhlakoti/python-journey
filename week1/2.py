username = 'kartik'
password = input('something is the password what is it : ')
if username == 'kartik':
    if password=='something':
        print('hello  kartik!  ' ,end = '' )
        print('Access granted')
    elif password == 'karma':
        print('hello  kartik!  ' ,end = '' )
        print('Access granted')
    else:
        print('Access denied intruder')
# ----------------------------------------------------------------------------
name = 'kartik'
age = int(input('Enter the age for verification : '))
# if  name == 'kartik':
#     print('Hi kartik')
#    --- this will make the jump outside the if loop
if age<12:
    print('you are not kartik , kiddo.')
elif age >= 18:
    print('get out of puberty first!')
elif age > 100:
    print('you still alive ?')
elif age == 20:
    print('Hey welcome back ! kartik')
else:
    print('not correct')
today_is_opposite_day = False
if today_is_opposite_day==True:
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False
if today_is_opposite_day == True:
    say_it_is_opposite_day = not say_it_is_opposite_day
if say_it_is_opposite_day == True:
    print('today is opposite day.')
else:
    print('today is the opposite day.')
# ----------------------------------------------------------------------------
print('Enter TB or GB for the advertised unit : ')
unit = input('-->')
# calculation of the lied amount
if unit == 'TB' or unit =='tb':
    error_of= 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
    error_of= 1000000000/ 1073742824

print('Enter the advertised capacity without unit : ')
advertised_capacity = input('-->')
advertised_capacity = float(advertised_capacity)

# rounding it to nearest hundredths and then to str(concatenate)
real_capacity = str(round(advertised_capacity * error_of , 2))

print('The actual capacity is ' + real_capacity + ' ' + unit)