# Python Cheat Sheet for High School CS Students

# 1. Variables
# Variables are used to store data values.
# You can think of a variable as a container for storing data.

# Example:
name = "Alice"  # String variable
age = 16        # Integer variable
is_student = True  # Boolean variable


print("Name:", name)
print("Age:", age)
print("Is student:", is_student)
print("Height:", height)

# 2. Terminal Methods: print() and input()
# print() is used to display output to the terminal.
# input() is used to get input from the user via the terminal.

# Example:
user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")

# Example:
age_str = input("Enter your age: ")  # Input is always a string
age = int(age_str)  # Convert string to integer
print("You are", age, "years old.")

# 3. Conditionals (If-Else Statements)
# Conditionals are used to make decisions in your code.
# They execute different blocks of code based on whether a condition is true or false.

# Example:
temperature = 25

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's a pleasant day.")
else:
    print("It's a bit chilly.")

# 4. Data Types
# Python has several built-in data types, including:
# - Strings (str): Textual data
# - Integers (int): Whole numbers
# - Booleans (bool): True or False values
# - Lists: Ordered collections of items

# Strings
message = "Hello, World!"
print("String:", message)
print("First character:", message[0])  # Accessing characters in a string

# Integers
count = 150
print("Integer:", count)

# Booleans
is_valid = True
print("Boolean:", is_valid)

# Lists (Arrays)
# Lists are used to store multiple items in a single variable
# They are ordered, changeable, and allow duplicate values.

# Example:
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)
print("First fruit:", fruits[0])  # Accessing elements in a list

fruits.append("orange")  # Adding an element to the end of the list
print("Updated list:", fruits)

# 5. Password Checking Algorithm
# A simple example of a password checking algorithm

def check_password(password):
    # Define password criteria
   realPassword = 'xyz123'
   userAttempt = input('What is the Password?')
   if userAttempt == realPassword:
       print("Access Granted")
   else:
       print("Wrong Password")
