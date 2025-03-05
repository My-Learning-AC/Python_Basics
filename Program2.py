# Strings:
        #-----------------------------------------------
        phase = "ECEN Academy"
        print(phase.isupper())
        # Output: False
        #------------------------------------------------

        #------------------------------------------------
        phase = "ECEN Academy"
        print(phase.upper().isupper())
        # Output: True
        #------------------------------------------------

        #------------------------------------------------
        phase = "ECEN Academy"
        print(phase.upper())
        print(phase)
        # Output: ECEN ACADEMY
        #         ECEN Academy
        #------------------------------------------------

        #------------------------------------------------
        phase = "ECEN Academy"
        print(len(phase))
        # Output: 12
        #------------------------------------------------

        #------------------------------------------------
        phase = "ECEN Academy"
        print(phase[0:4])
        # Output: ECEN
        #------------------------------------------------

        #------------------------------------------------
        phase = "ECEN Academy"
        print(phase.index("Aca"))
        # Output: 5
        #------------------------------------------------

        #------------------------------------------------
        phase = "ECEN Academy"
        print(phase.replace("Academy", "Scool"))
        print(phase)
        # Output: ECEN Scool
        #         ECEN Academy
        #------------------------------------------------

0000000000000000000000000000000000000000000000000000000000000000000000

# Numbers:
        #------------------------------------------------
        my_number = 50
        print(str(my_number) + " is my favorate")
        # Output: 50 is my favorate
        #------------------------------------------------

        # abs() - absolute value
        #------------------------------------------------
        my_number = -5
        print(abs(my_number))
        # Output: 5
        #------------------------------------------------

        # pow() - power of base
        #------------------------------------------------
        print(pow(3, 2))
        # Output: 9
        #------------------------------------------------

        #------------------------------------------------
        print(max(6, 2))
        # Output: 6
        #------------------------------------------------

        #------------------------------------------------
        print(min(6, 2))
        # Output: 2
        #------------------------------------------------

        #------------------------------------------------
        print(round(5.987))
        # Output: 6
        print(round(5.287))
        # Output: 5
        #------------------------------------------------

        #------------------------------------------------
        from math import *
        print(floor(3.9))
        # Output: 3
        #------------------------------------------------

        #------------------------------------------------
        from math import *
        print(ceil(3.2)
        # Output: 4
        #------------------------------------------------

        #------------------------------------------------
        from math import *
        print(sqrt(36))
        # Output: 6.0
        #------------------------------------------------

        #------------------------------------------------
        from math import *
        print(sqrt(35))
        # Output: 5.916079783099616
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# Input from user
        #------------------------------------------------
        name = input("Enter your name: ")
        print("Hii " + name + " !")
        # Input:  Enter your name: Dharani
        # Output: Hii Dharani !
        #------------------------------------------------

        #------------------------------------------------
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        result = float(num1) + float(num2)
        print(result)
        # Enter first number: 5.3
        # Enter second number: 3
        # 8.3
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# List
        #------------------------------------------------
        friends = ["Ram", "Sam", "Jadu", 2, False]
        print(friends)
        # Output: ['Ram', 'Sam', 'Jadu', 2, False]
        #------------------------------------------------

        #------------------------------------------------
        friends = ["Ram", "Sam", "Jadu", 2, False]
        print(friends[2])
        # Output: Jadu
        #------------------------------------------------

        #------------------------------------------------
        friends = ["Ram", "Sam", "Jadu", 2, False]
        print(friends[-4])
        # Output: Sam
        #------------------------------------------------

        #------------------------------------------------
        friends = ["Ram", "Sam", "Jadu", 2, False]
        print(friends[1:])
        # Output: ['Sam', 'Jadu', 2, False]
        #------------------------------------------------

        #------------------------------------------------
        friends = ["Ram", "Sam", "Jadu", 2, False]
        print(friends[1:3])
        # Output: ['Sam', 'Jadu']
        #------------------------------------------------

        #------------------------------------------------
        friends = ["Ram", "Sam", "Jadu", 2, False]
        friends[1] = 'Madhu'
        print(friends)
        # Output: ['Ram', 'Madhu', 'Jadu', 2, False]
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# List Functions
        #------------------------------------------------
        lucky_numbers = [4, 5, 7, 8, 3, 9]
        friends = ["Ram", "Sam", "Jadu", "Madhu"]
        friends.extend(lucky_numbers)
        print(friends)
        # Output: ['Ram', 'Sam', 'Jadu', 'Madhu', 4, 5, 7, 8, 3, 9]
        #------------------------------------------------

        #------------------------------------------------
        friends = ["Ram", "Sam", "Jadu", "Madhu"]
        friends.append("Roshan")
        print(friends)
        # Output: ['Ram', 'Sam', 'Jadu', 'Madhu', 'Roshan']
        #------------------------------------------------

        #------------------------------------------------
        friends = ["Ram", "Sam", "Jadu", "Madhu"]
        friends.insert(1, "Roshan")
        print(friends)
        # Output: ['Ram', 'Roshan', 'Sam', 'Jadu', 'Madhu']
        #------------------------------------------------

        #------------------------------------------------
        friends = ["Ram", "Sam", "Jadu", "Madhu"]
        friends.remove("Sam")
        print(friends)
        # Output: ['Ram', 'Jadu', 'Madhu']
        #------------------------------------------------

        #------------------------------------------------
        friends = ["Ram", "Sam", "Jadu", "Madhu"]
        friends.clear()
        print(friends)
        # Output: []
        #------------------------------------------------

        #------------------------------------------------
        friends = ["Ram", "Sam", "Jadu", "Madhu"]
        friends.pop()
        print(friends)
        # Output: ['Ram', 'Sam', 'Jadu']
        #------------------------------------------------

        #------------------------------------------------
        friends = ["Ram", "Sam", "Jadu", "Madhu"]
        print(friends.index("Jadu"))
        # Output: 2
        #------------------------------------------------

        #------------------------------------------------
        friends = ["Ram", "Sam", "Sam", "Jadu", "Madhu", "Sam"]
        print(friends.count("Sam"))
        # Output: 3
        #------------------------------------------------

        #------------------------------------------------
        friends = ["Ram", "Sam","Arun", "Sam", "Jadu", "Madhu", "Sam"]
        friends.sort()
        print(friends)
        # Output: ['Arun', 'Jadu', 'Madhu', 'Ram', 'Sam', 'Sam', 'Sam']
        #------------------------------------------------

        #------------------------------------------------
        lucky_numbers = [4, 5, 1, 9, 3, 5]
        lucky_numbers.sort()
        print(lucky_numbers)
        # Output: [1, 3, 4, 5, 5, 9]
        #------------------------------------------------

        #------------------------------------------------
        lucky_numbers = [4, 5, 1, 9, 3, 5]
        lucky_numbers.reverse()
        print(lucky_numbers)
        # Output: [5, 3, 9, 1, 5, 4]
        #------------------------------------------------

        #------------------------------------------------
        numbers = [4, 5, 1, 9, 3, 5]
        copy_num = numbers.copy()
        print(copy_num)
        # Output: [4, 5, 1, 9, 3, 5]
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# Tuples
        #------------------------------------------------
        coordinates = (4, 5)
        # coordinates[1] = 10   # Touples are not modified just like constant
        print(coordinates[0])
        # Output: 4
        #------------------------------------------------

        #------------------------------------------------
        coordinates = [(4, 5), (3, 5), (8, 4)]  # Touples inside a list
        print(coordinates[0])
        # Output: (4, 5)
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# Functions
        #------------------------------------------------
        def say_hi():
        print("Hello User")

        print("Top")
        say_hi()
        print("Bottom")
        # Output: Top
        #         Hello User
        #         Bottom
        #------------------------------------------------

        #------------------------------------------------
        def say_hi(name, age):
        print("Hello " + name + " you are " + str(age) + " years old")

        say_hi("Ram", 25)
        say_hi("Shyam", 32)
        # Output: Hello Ram you are 25 years old
        #         Hello Shyam you are 32 years old
        #------------------------------------------------

# Return Statement
        #------------------------------------------------
        def cube(num):
        return num * num * num

        print(cube(3))
        # Output: 27
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# If-elif-else Statements
        #------------------------------------------------
        is_male = False
        is_tall = True

        if is_male and is_tall:
        print("You are a tall male")
        elif is_male and not (is_tall):
        print("You are a short male")
        elif not(is_male) and is_tall:
        print("You are not a male but tall")
        else:
        print("You neither male and nor tall")
        # Output: You are not a male but tall
        #------------------------------------------------

        #------------------------------------------------
        def max_num(num1, num2, num3):
        if num1 > num2 and num1 > num3:
                return num1
        elif num2 > num1 and num2 > num3:
                return num2
        else:
                return num3

        print(max_num(1, 2, 3))
        # Output: 3
        #------------------------------------------------

        #------------------------------------------------
        def find_animal(animal_name):
        if animal_name == 'dog':
                return 'Dog'
        elif animal_name == 'cat':
                return 'Cat'
        elif animal_name == 'horse':
                return 'Horse'
        elif animal_name == 'mouse':
                return 'Mouse'
        else:
                return "This is not a animal"

        animal = find_animal('dog')
        print(animal)
        # Output: Dog
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# Dictionaries
        #------------------------------------------------
        month_conversion = {
        "Jan": "January",
        "Fab": "February",
        "Mar": "March",
        "Apr": "April",
        "May": "May",
        "Jun": "June",
        "Jul": "July",
        "Aug": "August",
        "Sep": "September",
        "Oct": "October",
        "Nov": "November",
        "Dec": "December"
        }

        print(month_conversion["Nov"])
        # Output: November

        # print(month_conversion.get("Aug")) // We can access by this command also
        # Output: August
        #------------------------------------------------

        #------------------------------------------------
        month_conversion = {
        0: "January",
        43: "February"
        }

        print(month_conversion[43])
        # Output: February
        #------------------------------------------------

        #------------------------------------------------
        month_conversion = {
        0: "January",
        43: "February"
        }

        print(month_conversion.get(3))
        # Output: None
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# While Loop
        #------------------------------------------------
        i = 1
        while i <= 5:
        print(i)
        i += 1

        print("Done with loop")
        # Output: 1
        #         2
        #         3
        #         4
        #         5
        #         Done with loop
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# For loop
        #------------------------------------------------
        for letter in "ECEN":
        print(letter)
        # Output: E
        #         C
        #         E
        #         N
        #------------------------------------------------

        #------------------------------------------------
        friends = ["Ram", "Sam", "Jadu"]
        for friend in friends:
        print(friend)
        # Output: Ram
        #         Sam
        #         Jadu
        #------------------------------------------------

        #------------------------------------------------
        for index in range(5):
        print(index)
        # Output: 0
        #         1
        #         2
        #         3
        #         4
        #------------------------------------------------

        #------------------------------------------------
        for index in range(5, 10):
        print(index)
        # Output: 5
        #         6
        #         7
        #         8
        #         9
        #------------------------------------------------

        #------------------------------------------------
        friends = ["Ram", "Sam", "Jadu"]
        for index in range(len(friends)):
        print(friends[index])
        # Output: Ram
        #         Sam
        #         Jadu
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

        # 2D Lists & Nested Loop
        #------------------------------------------------
        number_grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0]
        ]

        print(number_grid[1][2])
        # Output: 6
        #------------------------------------------------

        #------------------------------------------------
        number_grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0]
        ]

        for row in number_grid:
        for col in row:
                print(col)
        # Output: 1
        #         2
        #         3
        #         4
        #         5
        #         6
        #         7
        #         8
        #         9
        #         0
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# Build a Translator
        #------------------------------------------------
        def translate(phrase):
        translation = ""
        for letter in phrase:
                if letter in "AEIOUaeiou":
                translation += "g"
                else:
                translation += letter
        return translation

        print(translate(input("Enter a phase: ")))
        # Enter a phase: COMPLETE
        # Output:        CgMPLgTg
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# Comment
        #------------------------------------------------
        '''
        You can write
        anythig into this
        because it will be
        treated as multiple
        line comments by
        python
        '''

        print("Comments in python")
        # Output: Comments in python
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# Try Except
        #------------------------------------------------
        try:
        number = int(input("Enter a number: "))
        print(number)
        except:
        print("Invalid input")

        # Enter a number: 34
        # Output:         34
        # Enter a number: shdd
        # Output          Invalid input
        #------------------------------------------------

        #------------------------------------------------
        try:
        value = 10/0
        number = int(input("Enter a number: "))
        print(number)
        except ZeroDivisionError:
        print("Divide by zero")
        except ValueError:
        print("Invalid input")
        # Output: Divide by zero
        #------------------------------------------------

        #------------------------------------------------
        try:
        #value = 10/0
        number = int(input("Enter a number: "))
        print(number)
        except ZeroDivisionError:
        print("Divide by zero")
        except ValueError:
        print("Invalid input")
        # Enter a number: df
        #Output:          Invalid input
        #------------------------------------------------

        #------------------------------------------------
        try:
        value = 10/0
        number = int(input("Enter a number: "))
        print(number)
        except ZeroDivisionError as err:
        print(err)

        # Output: division by zero
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# Reading Files
        #------------------------------------------------
        # Create a .tct file named Employee.txt in the same directory of python file
        # Content in the file: Hii everyone
        #                      My name is .........
        #                      I am learning python

        employee_file = open("Employee.txt","r")
        print(employee_file.readable())
        employee_file.close()
        # Output: True
        #------------------------------------------------

        #------------------------------------------------
        employee_file = open("Employee.txt","w")
        print(employee_file.readable())
        employee_file.close()
        # Output: False
        #------------------------------------------------

        #------------------------------------------------
        employee_file = open("Employee.txt","r")
        print(employee_file.read())
        employee_file.close()
        # Output: Hii everyone
        #         My name is .........
        #         I am learning python
        #------------------------------------------------

        #------------------------------------------------
        employee_file = open("Employee.txt","r")
        print(employee_file.readline())
        employee_file.close()
        # Output: Hii everyone
        #------------------------------------------------

        #------------------------------------------------
        employee_file = open("Employee.txt","r")
        print(employee_file.readline())
        print(employee_file.readline())
        employee_file.close()
        # Output: Hii everyone
        #         My name is .........
        #------------------------------------------------

        #------------------------------------------------
        employee_file = open("Employee.txt","r")
        print(employee_file.readlines())
        employee_file.close()
        # Output: ['Hii everyone\n', 'My name is .........\n', 'I am learning python']
        #------------------------------------------------

        #------------------------------------------------
        employee_file = open("Employee.txt","r")
        print(employee_file.readlines()[1])
        employee_file.close()
        # Output: My name is .........
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# Writing to Files
        #------------------------------------------------
        # Create a .tct file named Employee.txt in the same directory of python file
        # File Contents: Shyam - Salesman
        #                Ram   - Management
        #                Jadu  - Team Leader

        employee_file = open("Employee.txt","a")
        employee_file.write("\nToby - Human Resources")
        employee_file.close()

        # Now the File Contents: Shyam - Salesman
        #                        Ram   - Management
        #                        Jadu  - Team Leader
        #                        Toby - Human Resources
        #------------------------------------------------

        #------------------------------------------------
        # File Contents: Shyam - Salesman
        #                Ram   - Management
        #                Jadu  - Team Leader
        employee_file = open("Employee.txt","w")  # if there are not present the file, then this will create a new file 
        employee_file.write("\nToby - Human Resources")
        employee_file.close()
        # Now the File Contents: Toby - Human Resources
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# Modules and Pip
        #------------------------------------------------

        # File2.py contains:
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
         import random
         
         feet_in_mile = 5280
         meters_in_kilometer = 1000
         beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]
        
         def get_file_ext(filename):
             return filename[filename.index(".") + 1:]
        
         def roll_dice(num):
             return random.randint(1, num)
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        import File2

        print(File2.roll_dice(10))
        # Output: 9
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# Classes & Objects // class-(python) = strunture-(C) //
        #------------------------------------------------

        # File2.py contains:
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        class Student:

        def __init__(self, name, major, gpa, is_on_probation):
                self.name = name
                self.major = major
                self.gpa = gpa
                self.is_on_probation = is_on_probation
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        from Student import Student

        student1 = Student("Jim", "Business", 3.1, False)
        student2 = Student("Ram", "Arts", 5.3, True)

        print(student1.name)
        print(student2.major)
        # Output: Jim
        #         Arts
        #------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# Building aMultiple Choice Quiz
        #-------------------------------------------------------------------------

        # Question.py contains:
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        class Question:
        def __init__(self, question, answer):
                self.question = question
                self.answer = answer
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        from Question import Question

        question_prompts = [
        "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
        "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
        "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
        ]

        questions = [
        Question(question_prompts[0], "a"),
        Question(question_prompts[1], "c"),
        Question(question_prompts[2], "b")
        ]

        def run_test(questions):
        score = 0
        for question in questions:
                answer = input(question.question)
                if answer == question.answer:
                score += 1
        print("You got " + str(score) + "/" + str(len(questions)) + " correct")

        run_test(questions)

        # Output: What color are apples?
        #         (a) Red/Green
        #         (b) Purple
        #         (c) Orange
        #         
        #         a
        #         What color are Bananas?
        #         (a) Teal
        #         (b) Magenta
        #         (c) Yellow
        #         
        #         c
        #         What color are strawberries?
        #         (a) Yellow
        #         (b) Red
        #         (c) Blue
        #         
        #         b
        #         You got 3/3 correct
        #--------------------------------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

# Object Functions
        #--------------------------------------------------------------------------

        # Question.py contains:
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        class Student:

        def __init__(self, name, major, gpa):
                self.name = name
                self.major = major
                self.gpa = gpa

        def on_honor_roll(self):
                if self.gpa >= 3.5:
                return True
                else:
                return False

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        from Student import Student

        student1 = Student("Ram", "Accounting", 3.1)
        student2 = Student("Shyam", "Business", 3.8)

        print(student1.on_honor_roll())

        # Output: False
        #--------------------------------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000

        # Inheritance
        #--------------------------------------------------------------------------
        # Chef.py contains:
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        class Chef:

        def make_chicken(self):
                print("The chef makes a chicken")

        def make_salad(self):
                print("The chef makes a salad")

        def make_special_dish(self):
                print("The chef makes a dish")

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        from Chef import Chef

        myChef = Chef()
        myChef.make_chicken()
        # Output: The chef makes a chicken
        #--------------------------------------------------------------------------

        #--------------------------------------------------------------------------
        # Chef.py contains:
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        class Chef:

        def make_chicken(self):
                print("The chef makes a chicken")

        def make_salad(self):
                print("The chef makes a salad")

        def make_special_dish(self):
                print("The chef makes a dish")

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # ChineseChef.py contains:
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        from Chef import Chef

        class ChineseChef(Chef):
        def make_fried_rice(self):
                print("The chef makes fried rice")

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        from ChineseChef import ChineseChef

        myChineseChef = ChineseChef()
        myChineseChef.make_chicken()
        # Output: The chef makes a chicken
        #--------------------------------------------------------------------------

000000000000000000000000000000000000000000000000000000000000000000000000