#a function is a block of code. You can define it once and call it as needed 

def display_welcome():
    print("Welcome to the Snack Shack!")
    print("Most snacks are $4.00 each.")

def calculate_total(quantity,unit_price = 4):
    total = quantity * unit_price 
    return total

def display_output(item_name, quantity, total):
    print(f"Snack: {item_name}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total:.2f}")

#function to prompt for an integer for How many? Keep prompting until a valid integer is entered and return the integer
def get_valid_quantity():
    while True:
        try:
            return int(input("How many? "))            
        except ValueError:
            print("Must be a whole number")        
           

UNIT_PRICE = 2.99

display_welcome()
item_name = input("Snack name: ")
quantity = get_valid_quantity()
#total = calculate_total(quantity,UNIT_PRICE) #override the default
#total = calculate_total(quantity)#using the default
total = calculate_total(quantity = quantity, unit_price = UNIT_PRICE)
display_output(item_name, quantity, total)