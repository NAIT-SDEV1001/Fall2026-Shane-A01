#Create a new list (use a loop) of each value doubled
numbers = [2,4,6,8]
doubled = []

for number in numbers:    
    doubled.append(number * 2)
print(doubled)
#list comprehension
#Shortcut to create a new list
numbers = [2,4,6,8]
doubled = [number * 2 for number in numbers]
print(doubled)
#Create a new list of these names in upper case
names = ["Fred", "Wilma", "Barney"]
upper_case = [name.upper() for name in names]
print(upper_case)

#if
#Create a new list of only numbers > 10 
#Without list comprehension
numbers = [3,8,12,5,20,31,4]
large_numbers = []

for number in numbers:
    if number > 10:
        large_numbers.append(number)
print(large_numbers)

#list comprehension
numbers = [3,8,12,5,20,31,4]
large_numbers = [number for number in numbers if number > 10]
print(large_numbers)

