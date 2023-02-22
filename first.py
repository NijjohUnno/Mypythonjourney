##### MY Python Journey
'''
msg = "Hello Oti"
print("Welcome Aboard")
print(msg)
'''

## Indentation
'''
if 5 > 2: 
    print("Five is greater than two")
'''

##VARIABLES - used to temporarily store data in comp memory

'''
price = 10 #integer
rating = 4.7 #float
is_published = False #boolean
name = "Oti" #string
print(price)
'''

##Hospital quiz
'''
name = "John Smith" #string
age = 20 #int
is_new_patient = True  #boolean

'''
#INPUT quiz

'''
name = input("Enter your name ")
color = input("What's your favourite color? ")
print(name +" likes " +color)
'''
#TYPE conversion
'''
birth_year = int(input("Which year were you born? "))
age = 2023 - birth_year
print("You are ", + age ," years old")
print(type(birth_year))
print(type(age))
'''

#Type quiz -- ask a user their weight (in pounds) convert it to kilograms and print

'''
weight = int(input("Enter your weight in Pounds "))
con_weight = weight * 0.45
print("Your weight is ", +con_weight ," kilograms")
'''

#STRINGS
'''
course = "Python's Course for beginners" #using double quotes
course_2 = 'Python for "Beginners"'      #using single quotes
                                         #using tripple quotes

'''
'''
course_3 = '''
'''Hello Team,

Hope this email finds you well. 
Kindly use this 'link' to access a spotify playlist incase it doesn't.
'''
'''
print(course[-1])
print(course_2)
print(course_3) 
'''

#Formatted Strings

'''
first = "John"
last = "Doe"
msg = f'{first} [{last}] is a coder'
print(msg)
'''
#String Methods
'''
course = "Python for beginners"
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('P')) #.find is case-sensitive
print(course.replace('beginners','Absolute beginners')) #.replace is case-sensitive
print('Python' in course)
'''

#ARITHMETIC OPERTAIONS
#numbers : integers, floats
'''
print(10 - 3)
print(10 + 3)
print(10 * 3)
print(10 // 3)  #returns integer
print(10 / 3)
print(10 ** 3) #exponential
print(10 % 3)
'''

#Argumentated assignment operator
'''
x = 10
x +=3
print(x)
'''
#operator precedence   ...order of operations(() ->** -> */ -> +-)
'''
x = 10 + 3 * 2
y = 10 + 3 + 2**2
print (x)
'''

#MATH functions (round, abs, )
'''
import math
x = 2.9
print(round(x))
print(math.ceil(x))
print(math.floor(x))
'''

#IF STATEMENTS
'''
is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("Enjoy your day")
'''
#IF Statement exercise
'''
price = 10000
good_credit = False

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Please Pay ${down_payment}")
'''

#LOGICAL OPERATORS (and, or, not)
'''
has_high_income = True
has_good_credit = False
has_criminal_record = False

if has_high_income and not has_criminal_record:
    print("Eligible for a loan")
else:
    print("Kindly work on your credit score")
'''

#COMPARISON OPERATORS ( > , < , == , !=)
'''
x = int(input("Enter Temperature "))
if x > 30:
    print("It's a hot day")
elif x < 10:
    print("It's a cold")
else:
    print("It's neither hot or cold")
'''

#Comparison operator assignment
'''
name = input("Enter your name ")

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good")
'''

#PROJECT: Weight converter

weight = int(input("Enter your weight "))


