def display_welcome():
    print("Welcome to the Snack Shack!")
    print("Most snacks are $4.00 each.")

def display_output(item_name, quantity, total):
    print(f"Snack: {item_name}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total:.2f}")