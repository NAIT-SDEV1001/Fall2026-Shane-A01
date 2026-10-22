# Solutions for argument_unpacking.py practice: Questions 7 and 8.

# Question 7 - Delivery label
# These are ordinary parameters, not *args or **kwargs parameters.
def print_delivery(customer, city, parcels):
    print(f"{customer} has {parcels} parcels going to {city}.")


# Question 8 - Pet introduction
def introduce_pet(name, species, age):
    print(f"{name} is a {species} aged {age}.")



print("Question 7 - Delivery label")
delivery = ("Maya", "Edmonton", 3)
# * unpacks values by position: customer, city, then parcels.
# The tuple order must match the parameter order.
print_delivery(*delivery)

print("\nQuestion 8 - Pet introduction")
pet = {"age": 4, "name": "Pickles", "species": "cat"}
# ** unpacks entries into keyword arguments.
# Keys must match the parameter names; their dictionary order can differ.
introduce_pet(**pet)


