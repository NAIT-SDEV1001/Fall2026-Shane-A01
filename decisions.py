#decisions allow us to control the flow of the code

age = 17

if age >=18:
    print("You are an adult")
    print("Have a groovy day!")

print("This is fun!")#always executes

# #comparison operators: ==,!=, <, >, <=, >=

name = input("Enter your name: ")
if name == "Shane":
    print("Awesome name!")

# #remember it is case sensitive
# #safe comparison ignoring case
name = input("Enter your name: ")
if name.upper() == "SHANE": #compare upper case of user name
    print("Awesome name!")

#Else
name = input("Enter your name: ")
if name.upper() == ("SHANE"):
    print("Awesome name!")#if condition it True
else:
    print("Nobodys perfect.....")#if condition is false

print("Have a groovy day!")#always

grade = 40
if grade >= 50:
    print("Pass")
else:
    print("Fail")

grade = 12
# multiple conditions 
if grade >= 80:
    print("Honors!")
    print("You are smart!")
elif grade >= 50:
    print("pass")
elif grade == 0:
    print("Did you show up?")
else: #if none of the above conditions are true
    print("Fail")
    print("Please try again")

print("Have a groovy day!")


