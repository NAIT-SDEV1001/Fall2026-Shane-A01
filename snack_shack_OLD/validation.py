def get_valid_quantity():
    while True:
        try:
            return int(input("How many? "))            
        except ValueError:
            print("Must be a whole number")