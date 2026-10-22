# Dictionaries - store data in key-value pairs
# Keys are unique. Strings or numbers
# Values can be anything(strings, bool, int... , dictionaries)

#Example
student = {"name":"Homer","age":44,"email":"Homer@gmail.com"}

#Access values by the key
print (student["name"])#retrieve a value
student["age"] = 42#update a value
student["city"] = "Springfield"#Create a new key/value

#new key-value from the user
key = input("Enter a new key: ")
value = input("Enter a value for that key: ")
student[key] = value

#remove a key-value
del student["email"]

print(student)

#using a key that does not exist is a KeyError
# del student["favorite_color_smartie"]

#check if key exists:
if "favorite_color_smartie" in student:
    del student["favorite_color_smartie"]

#Use get to retrieve value
#returns None if key does not exist
print(student.get("favorite_color_smartie"))
#OR return a different value
print(student.get("favorite_color_smartie","N/A"))

#Dictionaries as values
inventory = {
            "apples":{"stock_count":5,"price":.30},
            "bananas":{"stock_count":55,"price":.20},
            "oranges":{"stock_count":40,"price":.25},
}

print (inventory["apples"]["price"])

#Loop through a dictionary
student = {"Homer":30,"Lisa":98,"Bart":45,"Marge":70}
#keys
for key in student:#by default keys are returned
    print(f"{key}: {student[key]}")

#Loops through the values:
#get average of all the grades
total = 0
for grade in student.values():
    total += grade
print(f"Average grade: {total/len(student)}")

#Retrieve both key and values
for name, grade in student.items():
    print(f"{name}: {grade}")

#sort by the key
for name, grade in sorted(student.items()):
    print(f"{name}: {grade}")
#Reverse
for name, grade in sorted(student.items(),reverse=True):
    print(f"{name}: {grade}")

inventory = {"apples":0,"bananas":0,"oranges":0}
purchases = ["apples","bananas","apples","oranges","apples"]
#update inventory
for item in purchases:
    inventory[item] += 1
#display current inventory
for item,count in inventory.items():
    print(f"{item}: {count}")


#Add the boxes of purchases to the inventory.
#Result
# {"apples":3,"bananas":1,"oranges":1}

#print out
#apples: 3
#bananas: 1
#oranges: 1

