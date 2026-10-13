#Exception handling gives a way to gracefully handle errors and keep code executing
#Try/except blocks

sum = 0
count= 0
while True:
    number = int(input("Enter a number: "))
    if number == -1:
        break
    sum += number
    count += 1

average = sum/count
print(f"The average is: {average}")

#use try/except
sum = 0
count = 0
while True:
    try:
        number = int(input("Enter a number: "))
    except ValueError as error_message:
        print(f"Must be a number: {error_message}")
        continue
    if number == -1:
        break
    sum += number
    count += 1
try:
    average = sum/count
    print(f"The average is: {average}")
except ZeroDivisionError as error_message:
    print(f"No numbers were entered: {error_message}")

#Raise Custom exceptions for our own rules
#cannot be less than -1
#else: 
sum = 0
count = 0
while True:
    try:
        number = int(input("Enter a number: "))
        if number < -1:
            raise ValueError ("Negative numbers are not allowed, except -1 to quit")
    except ValueError as error_message:
        print(f"Invalid input. Must be a number >= -1: {error_message}")
        continue
    else: #optional
        print("number accepted")
    if number == -1:
        break
    sum += number
    count += 1
try:
    average = sum/count
    print(f"The average is: {average}")
except ZeroDivisionError as error_message:
    print(f"No numbers were entered: {error_message}")


#check multiple exceptions of one try:
try:
    number = int(input("Enter a number: "))
    result = 100/number
except ValueError: #using the error_message is optional:
    print("You must enter an integer")
except ZeroDivisionError:
    print("Cannot divide by 0. Number must be > 0")
else:#no exceptions occured in the try 
    print(f"The result is {result}")

