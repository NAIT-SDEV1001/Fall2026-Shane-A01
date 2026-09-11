# 1.
# Ask the user for a temperature in Celsius and convert it to Fahrenheit.
# get celcius
celsius = float(input("Enter a temperature in Celsius: "))
#calculate to fahrenheit
fahrenheit = celsius * 9 / 5 + 32
# display fahrenheit
print(f"Celsius: {celsius} => Fahrenheit: {fahrenheit:.2f}")

# 2.
# Ask the user for a name, an adjective, a verb (past tense) and a place. Print a silly sentence using them.
name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
past_tense_verb = input("Enter a verb in the past tense: ")
place = input("Enter a place: ")

print(f"{name}, the {adjective} programmer, {past_tense_verb} all the way to {place}!")

3.
Ask the user for the width and height of a rectangle. There could be decimals. Calculate and display the width, height, area, and perimeter. Calculations print the results rounded to 3 decimal places.
width = float(input("Enter the rectangle's width: "))
height = float(input("Enter the rectangle's height: "))

area = width * height
perimeter = 2 * (width + height)

print(f"Width: {width:.3f}")
print(f"Height: {height:.3f}")
print(f"Area: {area:.3f}")
print(f"Perimeter: {perimeter:.3f}")

# 4.
# Ask for the price of an item and the quantity purchased. Display the amount of the total including GST.

price = float(input("Enter the price of one item: $"))
quantity = int(input("Enter the quantity purchased: "))

GST = 0.05

subtotal = price * quantity
gst = subtotal * GST
total = subtotal + gst

print(f"Subtotal: ${subtotal:.2f}")
print(f"GST: ${gst:.2f}")
print(f"Total: ${total:.2f}")


# 5.
# Ask the user for a number of miles and print out how many kilometres it is. Display to 2 decimal places.
# The conversion rate is 1 mile = 1.609344 kilometers
KILOMETRES_PER_MILE = 1.609344

miles = float(input("Enter the number of miles: "))
kilometres = miles * KILOMETRES_PER_MILE

print(f"{miles} miles is {kilometres:.2f} kilometres.")

# 6.
# Ask the user for the distance they want to travel, the fuel consumption of their vehicle in l/100km and the price per litre. Display the cost for the trip!

# get distance, fuel consumption, price per litre from user
distance = float(input("Enter the distance in km: "))
fuel_consumption = float(input("Enter fuel consumption in L/100 km: "))
price_per_litre = float(input("Enter the price per litre: $"))

#Calculate the Cost
    # how many litres for distance?
litres_needed = distance * fuel_consumption / 100
    # multiply litres * price per litre
trip_cost = litres_needed * price_per_litre
#Display the Cost
print(f"Fuel needed: {litres_needed:.2f} litres")
print(f"Trip cost: ${trip_cost:.2f}")


#Populate 2 variables with 2 numbers from the user 
    #number1
    #number2
#Print the values in each variable
#Swap the values that are in the variables so the value in variable1 is placed in variable2 and vice versa
#print the values in each variable
number1 = input("Enter number 1: ")
number2 = input("Enter number 2: ")

print("Before Swap")
print (f"Number1: {number1}")
print (f"Number2: {number2}")

temp = number1
number1 = number2
number2 = temp

print("After Swap")
print (f"Number1: {number1}")
print (f"Number2: {number2}")
