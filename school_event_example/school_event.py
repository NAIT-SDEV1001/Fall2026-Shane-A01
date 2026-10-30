"""A separate school event program that reuses the snack_shack package."""

# Import three modules from the package.

# from snack_shack import display, pricing, validation
from snack_shack.display import display_welcome,display_receipt
from snack_shack.validation import get_valid_quantity
#Show both ways to import and how you call the functions after each way
def main():
    print("School Movie Night - Snack Sales")
    print()
    display.display_welcome()
    # display_welcome()

    item_name = input("What snack are we selling? ")
#STUDENT: get the valid quantity from the user. Must be >0 and an integer. Use get_valid_quantity() somewhere in your code
    # Reuse the package's input function.
    quantity = validation.get_valid_quantity()

    # The supplied function checks for integers but accepts zero and negatives.
    # This program adds the school event's rule: quantity must be positive.
    while quantity <= 0:
        print("Please enter a quantity greater than zero.")
        quantity = validation.get_valid_quantity()
#STUDENT: Get the total
    # Reuse the default price of $4.00 from the pricing module.
    total = pricing.calculate_total(quantity)

#STUDENT: display the total
    print()
    display.display_receipt(item_name, quantity, total)
    print("Thanks for supporting our school movie night!")

#STUDENT: How to ensure the mainline does not run if this file is imported?
# Run the mainline when this file is executed directly.
if __name__ == "__main__":
    main()
