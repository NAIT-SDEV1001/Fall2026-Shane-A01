def display_welcome():
    print("Welcome to Movie Night!")
    print("Ages 0-12: $8.00")
    print("Ages 13-64: $12.00")
    print("Ages 65 and older: $9.00")
    print("Everyone in one order must belong to the same age group.")

def display_receipt(quantity, ticket_price, total):
    print("\nYour Movie Night Receipt")
    print(f"Tickets: {quantity}")
    print(f"Price per ticket: ${ticket_price:.2f}")
    print(f"Total: ${total:.2f}")
    print("Enjoy the movie!")
