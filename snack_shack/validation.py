def get_valid_integer(prompt):
    while True:
        try:
            return int(input(f"{prompt}: "))            
        except ValueError:
            print("Must be a whole number")


print(get_valid_integer("Enter your favorite number"))
print(get_valid_integer("Enter your age"))

def get_non_empty_string(prompt):
    while True:
        value = input(f"{prompt}: ")
        if value.strip():#if after the strip() is executed there is still text then stop asking
            break
    return value




#if x has a value it will be evaluated as True in a decision
x = ""
if x:
    print("x has a value")
else:
    print("x does not have a value")