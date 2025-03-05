# Print function
#-------------------------------------------------
print("Hello World")      # print the string
#-------------------------------------------------


# variables and strings
#-------------------------------------------------
age = 20                  # age is a variable
price = 19.95             # price is a variable
first_name = "Dharani"    # first_name is a array that holds stringd
is_online = False         # is_online is a boolean variable
print(age)                # print a variable
#-------------------------------------------------


# Input function just like scanf
#-------------------------------------------------
name = input("What is your name? ")   # input is just like a scanf function and return whatever you entered
print("Hello " + name)
# print("Hello", name)

name = input()   # the exact thing
print(name)
#-------------------------------------------------


# Typecasting of data
#-------------------------------------------------
birth_year = input("Enter your birth year: ") # input function always returns strings
age = 2020 - int(birth_year)    # here we typecast the string into integer
print(age)

# Typecasting inbuilt functions
int()        # for converting into integer
float()      # for converting into float
bool()       # for converting into boolean expression
str()        # for converting into string
#-------------------------------------------------


# Sum of two numbers
#-------------------------------------------------
num1 = input("First: ")
num2 = input("Second: ")
result = float(num1) + float(num2)

# not use result = num1 + num2, It will give the String Output

print("Sum:", result)
#print("Sum: " + str(result))

num1 = float(input("First: "))
num2 = float(input("Second: "))
result = num1 + num2
print("Sum: " + str(result))
#-------------------------------------------------


#Various sub-functions of a variable
#-------------------------------------------------
course = "Python for Beginners"
print(course.upper())       # print the string into upper case
print(course)               # print the string as it is

course = "Python for Beginners"
print(course.find("y"))      # find the location of y into the string (i.e., - 1)

course = "Python for Beginners"
print(course.find("for"))    # output: 7 (find the location of 'for')

course = "Python for Beginners"
print(course.replace("for", "4"))  # output: Python 4 Beginner

course = "Python for Beginners"
print("Python" in course)          # Output: True
#-------------------------------------------------


# Arithmetic Operation
#-------------------------------------------------
print(10 + 3)  # Output : 13
print(10 - 3)  # Output : 7
print(10 * 3)  # Output : 30
print(10 ** 3) # Output : (10^3) = 1000
print(10 / 3)  # Output : 3.333333 (float)
print(10 // 3) # Output : 3        (Integer)
print(10 % 3)  # Output : 1

x = 10
x = x + 3
# can be use x += 3
#-------------------------------------------------


# Operator Precedence
#-------------------------------------------------
x = 10 + 3 * 2
print(x)         # Output: 16

x = (10 + 3) * 2
print(x)         # Output: 26
#-------------------------------------------------


# Comparison Operators
#-------------------------------------------------
x = 10
y = 13

x > y
x < y
x >= y
x <= y
x == y
x != y
#-------------------------------------------------


# Logical Operators
#-------------------------------------------------
price = 25
print(price > 10 and price < 30)   # Output: True

price = 25
print(not price > 10)              # Output: False

and
or
not
#-------------------------------------------------


# if-else Statement
#-------------------------------------------------
temperature = 25

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
print("Done")                            # Output: Done

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++

temperature = 12

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's a cold day")
print("Done")
#-------------------------------------------------


# Exercise
#-------------------------------------------------
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

# Input:  170, l
# Output: 76.5

# Input:  76, k
# Output: 168.8888..
#-------------------------------------------------


# While loop
#-------------------------------------------------
i = 1
while i <= 1_000:
    print(i)
    i += 1

#+++++++++++++++++++++++++++++++++++++

i = 1
while i <= 10:
    print(i * '*')   # (i * character) is different from (i - character)
    i += 1

# Output:
*
**
***
****
*****
******
*******
********
*********
**********
#-------------------------------------------------


# List
#-------------------------------------------------
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names)
names[0] = "JON"
print(names)
print(names[0 : 3])
print(names)

# Output:
['John', 'Bob', 'Mosh', 'Sam', 'Mary']
['JON', 'Bob', 'Mosh', 'Sam', 'Mary']
['JON', 'Bob', 'Mosh']
['JON', 'Bob', 'Mosh', 'Sam', 'Mary']
#-------------------------------------------------


# List Methods
#-------------------------------------------------
names = [1, 2, 3, 4, 5]
names.append(6)
print(names)
# Output: [1, 2, 3, 4, 5, 6]

names = [1, 2, 3, 4, 5]
names.insert(0, -1)
print(names)
# Output: [-1, 1, 2, 3, 4, 5]

names = [1, 2, 3, 4, 5]
names.remove(3)
print(names)
# Output: [1, 2, 4, 5]

names = [1, 2, 3, 4, 5]
names.clear()
print(names)
# Output: []

names = [1, 2, 3, 4, 5]
print(10 in names)
# Output: False

names = [1, 2, 3, 4, 5]
print(len(names))
# Output: 5  # length
#-------------------------------------------------


# For Loops
#-------------------------------------------------
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

# Using while loop
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# Output:
1
2
3
4
5
#-------------------------------------------------


# The Range Function
#-------------------------------------------------
numbers = range(5)
print(numbers)

# Output:  range(0, 5)
numbers = range(5)
for number in numbers:
    print(number)

# Output:
0
1
2
3
4


numbers = range(5, 10)
for number in numbers:
    print(number)

# Output:
5
6
7
8
9


numbers = range(5, 10, 2)
for number in numbers:
    print(number)

# Output:
5
7
9


for number in range(5):
    print(number)

# Output:
0
1
2
3
4#-------------------------------------------------


# Tuples
#-------------------------------------------------
numbers = [1, 2, 3]    # List []
numbers = (1, 2, 3)    # Touple ()
numbers[0] = 10        # This will generate an error as the touple is just like constant and can not be modified
#-------------------------------------------------

