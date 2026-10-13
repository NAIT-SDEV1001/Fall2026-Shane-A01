print("Shopping Total")
item_count = 0
total_cost = 0.0
price_input = input("Enter an item price (q to quit): ")

# Challenge: lower() allows either q or Q to quit.
while price_input.lower() != "q":
    price = float(price_input)
    total_cost += price
    item_count += 1
    price_input = input("Enter an item price (q to quit): ")

print(f"Items purchased: {item_count}")
print(f"Total cost: ${total_cost:.2f}")