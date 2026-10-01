TOPPING_COST = 2
topping_count = 0

toppings = []
#add variables to a list
#strip removes spaces at the start and end of strings
toppings.append(input("Enter a topping 1: ").strip().lower())
toppings.append(input("Enter a topping 2: ").strip().lower())
toppings.append(input("Enter a topping 3: ").strip().lower())
toppings.append(input("Enter a topping 4: ").strip().lower())
toppings.append(input("Enter a topping 5: ").strip().lower())
print()
#print out a numbered list of entered toppings
print("Requested toppings:")
for number, topping in enumerate(toppings, start=1):
    print(f"{number}. {topping}")
print()
#Create 2 tuples of banned toppings and sold out toppings
sold_out = ("mushrooms","bacon")
banned_toppings = ("pineapple")
#Loop through toppings display Adding, sold out or banned
    #sold out means it is in the sold out tuple
    #banned means it is in the banned tuple
    #when added increment a count
    #when added incerement the total cost
for topping in toppings:
    if topping in sold_out:
        print(f"Sorry, {topping} is sold out")
        continue
    if topping in banned_toppings:
        print(f"Sorry, {topping} is banned")
        continue
    print(f"Adding {topping}")
    topping_count = topping_count + 1
#A more common pattern is without continue
for topping in toppings:
    if topping in sold_out:
        print(f"Sorry, {topping} is sold out")        
    elif topping in banned_toppings:
        print(f"Sorry, {topping} is banned")        
    else:
        print(f"Adding {topping}")
        topping_count = topping_count + 1
        
total_cost = topping_count * TOPPING_COST
print()

print(f"{topping_count} toppings added")
print(f"Topping cost: ${total_cost:.2f}")
        





