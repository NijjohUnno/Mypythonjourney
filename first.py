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
'''
weight = int(input("Enter your weight "))
unit = input("Enter L for pounds and K for kgs ")

if unit.upper() == "L":
    mass = weight * 0.45
    print(f"You are {mass} KGs")
elif unit.upper() == "K":
    mass2 = weight / 0.45
    print(f"You are {mass2} Pounds")
else:
    print("Wrong unit of measure selected")
'''

#WHILE LOOP
'''
i = 1
while i <=5:
    print("x" * i)
    i = i+1
print("Done")
'''
#Guessing game
'''
secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count< guess_limit:
    num = int(input("Guess a number "))
    guess_count +=1
    if num == secret_number:
        print("Congratulations!")
        break
else:
    print("Wrong Guess")
'''
#Car game
'''
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        print("The car has started")
        if started:
            print("Car already started")
        else:
            started = True
            print("Car Started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
           started = False
           print("The car has stopped")
    elif command == "help":
        print('''
'''
start - to start the car
stop - to stop the car
quit - terminate session
        '''#)
'''
    elif command == "quit":
        break
    else:
        print("I dont understand your input")
'''

#FOR LOOP
'''
for item in "Python":
    print(item)

for name in ['Oti', 'Unno', 'Nijjoh']: #for loop in a list
    print(name)

for num in range(7, 10, 2):
    print(num)
'''
#FOR LOOP TEST
'''
price= [10, 20 ,30]
total = 0
for sum in price:
    total+= sum
print(total)
'''
#Nested Loop printing cordinates
'''
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

numbers = [5, 2, 5, 2, 2]

for num in numbers:
    test = ""
    for st in range(num): 
        test += "X"
    print(test)
'''

'''
# Create the variable for user input
user_input = ''
# Create the list to store the values
inputs = []

# The while loop
while user_input.lower() != 'done':
    # Check if there's a value in user_input
    if user_input:
        # Store the value in the list
        inputs.append(user_input)
    # Prompt for a new value
    user_input = input('Enter a new value, or done when done ')
print(inputs)

'''
#LISTS
'''
names= ['Alpha', 'Bravo','Charlie','Volcha']
print(names[2])
'''
'''
num = [2,4,5,3,3,2,4,4,3,4,3,5,7,7,8,6,9,3]
max_val = num[0]
for new in num:
    if new > max_val:
        max_val = new
print(max_val)
   ''' 
#matrix
'''
mat = [
    [2,4,5],
    [3,5,2],
    [5,6,3]
]
print(mat[2][2])
#print all items in a matrix
for row in mat:
    for item in row:
        print(item)
'''
#List methods --operations we can perform on a list
'''
numbers = [3,5,6,8,9,0,3,2,3]
numbers.append(22)
numbers.insert(0,11)
print(numbers)
'''
#removing duplicates
'''
numbers = [3,5,6,8,9,0,3,2,3]
uni = []
for number in numbers:
    if number not in uni:
        uni.append(number)
print(uni)

#Tuples --immutable
numbers = (9,6,7,5,6,6,6,5,4,1)
'''
#Dictionaries //each key should be unique
'''
customer = {
    "name":"John Oti",
    "age":40,
    "sport": "Tennis"
}
print(customer["sport"])
print(customer.get("age"))

phone = input("Phone: ")
gig_map = {
    "1": "One ",
    "2": "Two ",
    "3": "Three ",
    "4": "Four "
}
output = ""
for ch in phone:
    output += gig_map.get(ch, "!") + ""
print(output)
'''

#FUNCTIONS -- Container of a few lines of code that perform specific functions
'''
def greatings():
    print("Hello there")
    print("Welcome Aboard ")

print("Start")
greatings()
print("Stop")
'''
#Parameters
def greatings(name):
    print(f"Hello {name}")
    print("Welcome Aboard ")

greatings("Oti")
greatings("Unno")

