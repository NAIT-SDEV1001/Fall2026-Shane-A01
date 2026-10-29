def get_valid_age():

    while True:
        try:
            age = int(input("Enter age: "))
            if age < 0:
                raise ValueError
            return age
        except ValueError:
            print("Please enter a whole-number age of zero or greater.")

def get_valid_quantity():

    while True:
        try:
            quantity = int(input("Number of tickets: "))
            if quantity <= 0:
                raise ValueError
            return quantity
        except ValueError:
            print("Please enter a whole-number quantity greater than zero.")