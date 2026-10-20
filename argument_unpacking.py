# This functions expects 2 arguments: name and age
def show_info(name, age):
    print(f"{name} is {age} years old")

# store the persons info in a tuple
person = ("Alice",30)

# * unpacks the tuple into seperate positional arguments
show_info(*person)#unpacks into "Alice",30

# person info in a dictionary
person_dictionary = {"name":"Bob","age":25}

# ** unpacks the dictionary into seperate keyword arguments
show_info(**person_dictionary)#unpacks into (name = "Bob",age = 25)

# In a function definition(as parameters), *args and **kwargs collect arguments.
# Ina function call, * and ** unpack values into positional arguments and keyword arguments
