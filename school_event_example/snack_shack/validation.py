def get_valid_integer(prompt):
    while True:
        try:
            return int(input(f"{prompt}: "))            
        except ValueError:
            print("Must be a whole number")




def get_non_empty_string(prompt):
    while True:
        value = input(f"{prompt}: ")
        if value.strip():#if after the strip() is executed there is still text then stop asking
            break
        print("Snack name cannot be empty")
    return value


