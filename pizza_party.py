# Question 2 - Pizza party total

# Return the calculated amount so the caller can decide how to display it.
def calculate_order_total(pizza_count, price_each, delivery_fee=5.00):
    return pizza_count * price_each + delivery_fee


# Mainline: assume valid numeric input.
pizza_count = int(input("Number of pizzas: "))
price_each = float(input("Price per pizza: "))

# Omit the third argument to use the default delivery fee of $5.00.
delivery_total = calculate_order_total(pizza_count, price_each)

# Override the delivery fee with $0.00 for pickup.
pickup_total = calculate_order_total(pizza_count, price_each, 0.00)

print(f"Delivery total: ${delivery_total:.2f}")
print(f"Pickup total: ${pickup_total:.2f}")

# Optional challenge: uncomment these lines to try a custom delivery fee.
custom_fee = float(input("Custom delivery fee: "))
custom_total = calculate_order_total(pizza_count, price_each, custom_fee)
print(f"Custom delivery total: ${custom_total:.2f}")
