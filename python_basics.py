print("Intro to Python")
# Comment - does not execute
# To comment multiple
# lines , hightlite the lines 
# and ctrl /

# Case sensitive. 
# Extra spaces do not matter around commands, operators
# Spaces DO matter in indentation (code blocks). Indentation creates a code block
# Strings can us "" or ''. BE CONSISTENT
print('Hello World')
print("Hello World")
# "" are more common due to issues with appostrophes in strings ("O'clock")
print("It's a groovy day")

#Escape characters - provide ways insert values into strings and other behaviours 
print("It's a \"groovy\" day")
print('It\'s a "groovy" day!')
print("Hello\nWorld") #New line
print("Name:\tShane") #Tab
print("\\n how you go to a new line") #print an escape sequence 

# Variables
# A named box that holds a value
# values can change
# variable names contain only letters, numbers and _
# Cannot start with a number
# are written in snake_case
# in Python we do not explcitly declare variables before use
# Cannot be python keywords/reserved

# examples of assigning values to variables
first_name = "Shane" #String - written in quotes
age = 54 #integer
price = 12.25 #float
is_valid = True #Boolean (True/False)

age = 22

#Use a value in a variable
print(first_name)
print(age)

#String concatenation
# + is a string concatonation operator
print("Hello " + "World")
print("Hello " + first_name)

# When using + all values must be strings. We can cast the age to a string
print("Hello " + first_name + "! I see you are " + str(age) + " years old")

# You can use a comma and mix strings and numbers
print("Hello", first_name, "! I see you are", str(age), " years old")

#Preferred way (f strings)
print(f"Hello {first_name}! I see you are {age} years old")

# Constants - like a variable but is not supposed to change values
# Used to give a meaningfull name to a value
#Consants use SCREAMING_SNAKECASE
GST = .04

total = 100 * .05
print(total)
#BETTER
total = 100 * GST
print(total)

# User Input
# input returns a string
# name = input("Enter your name: ")
# age = input ("Enter your age: ")

# print(f"Hello {name}! You are {age} years old")

# prompt for 2 integers
# add them together
# display the sum
# number1 + number2 = sum
#int(), str(), float()

# number1 = input("Enter number 1: ")
# number2 = input("Enter number 2: ")

# sum = int(number1) + int(number2)

# print (f"{number1} + {number2} = {sum}")
# # OR
# number1 = int(input("Enter number 1: "))
# number2 = int(input("Enter number 2: "))
# sum = number1 + number2
# print (f"{number1} + {number2} = {sum}")

# Math Operators
print(4 + 2) #6
print(4 - 2) #2
print(4 * 2) #8
print(4 / 2) #2.0 / returns a float
print(9 // 4) #2 floor division (rounds down to closest whole number)
print (2 ** 3)#exponent
print (9 % 4) # 1 - Modulus

# Formatting numbers
total = 100.1234567
print(round(total,2))
print(round(total,6))

print(f"{total:.2f}")
print(f"{total:.6f}")

price = 100
print(f"{price:.2f}")

# MATH FUNCTIONS
# import imports the math module which contains math functions and constants
import math

test_value = 5.245435

print(math.ceil(test_value)) #ceiling (round up to next whole number)
print(math.floor(test_value)) #floor (round down to whole number)
print(math.pow(2,3)) #exponent
print(math.sqrt(9)) #square root
print(max(1,5,3,77,5,73)) # maximum
print(min(1,5,3,77,5,73)) # minimum


