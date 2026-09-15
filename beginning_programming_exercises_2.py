# Beginning Programming Exercises 2
# 1.
# One acre of land is equal to 43,560 square feet. Write a program that asks the user to enter the number of acres and display the number of square feet.
# Output:
# Acre to Square foot converter. How many acres do you have? 25
# You have 25 acres which is equal to: 1089000 square feet
# CONVERSION_RATE = 43560

# #get acres
# acres = (int(input("Acre to Square foot converter. How many acres do you have? ")))
# #calc sq ft
# square_feet = acres * CONVERSION_RATE
# #display sq ft
# print(f"You have {acres} acres which is equal to: {square_feet} square feet")

# 2.
# Write a program that asks the user to enter three test scores. The program should display each test score, as well as the average test of the users' scores.
# Output:
# Enter the first test score: 10
# Enter the second test score: 20
# Enter the third test score: 30
# Test Score 1: 10.0
# Test Score 2: 20.0
# Test Score 3: 30.0
# Average Score: 20.0

#get 3 numbers
# score1 = float(input("Enter the first test score: "))
# score2 = float(input("Enter the second test score: "))
# score3 = float(input("Enter the third test score: "))
# #show the 3 numbers
# print (f"Test Score 1: {score1}")
# print (f"Test Score 2: {score2}")
# print (f"Test Score 3: {score3}")
# #calculate average
# average = (score1 + score2 + score3)/3
# #Display average
# print(f"Average Score: {average}")

# 3.
# A bag of cookies holds 40 cookies. The calorie information on the bag claims that there are 10 "servings" in the bag and that a serving equals 300 calories. Write a program that asks the user to input how many cookies they ate and then reports how many total calories were consumed.
# Output:
# How many cookies did you eat? 25
# You ate 25 cookies
# Which is equal to: 1875.0 calories

#create constants
# COOKIES_PER_BAG = 40
# SERVICES_PER_BAG = 10
# CALORIES_PER_SERVING = 300
# #get number of cookies
# cookies = int(input("How many cookies did you eat? "))

# #calculate how much of the bag consumed
# percentage_of_bag_consumed = cookies/COOKIES_PER_BAG
# #how many calories in whole bag
# calories_per_bag = SERVICES_PER_BAG * CALORIES_PER_SERVING
# #calculate calories consumed
# calories_consumed = percentage_of_bag_consumed * calories_per_bag

# #display cookies and calories
# print (f"You ate {cookies} cookies")
# print (f"Which is equal to {calories_consumed} calories")

# 4.
# Ask the user for
# 
# number of pizzas (int)
# 
# price per pizza (float, dollars)
# 
# tip percent (float; e.g., 15 for 15%)
# 
# number of people sharing (int)
# Calculate and print: subtotal, tip amount, total, and amount per person.
# Formatting currency to 2 decimals. Display appropriate inputs and outputs.

# get input from user
# pizzas = int(input("How many pizzas? "))
# price_each = float(input("Price per pizza ($): "))
# tip_percent = float(input("Tip percent (e.g., 15 for 15%): "))
# people = int(input("How many people sharing? "))

# # calculate subtotal, tip, total, per_person
# subtotal = pizzas * price_each
# tip = subtotal * (tip_percent / 100)
# total = subtotal + tip
# per_person = total / people

# #display results
# print(f"Subtotal: ${subtotal:.2f}")
# print(f"Tip: ${tip:.2f}")
# print(f"Total: ${total:.2f}")
# print(f"Each person pays: ${per_person:.2f}")



# 5.
# Ask the user for a currency amount and display the number of dollars, quarters, dimes, nickels, and pennies in that amount. Display appropriate inputs and outputs.

#get dollar amount
amount = float(input("Enter a dollar amount (e.g. 3.87): "))
#change dollar amount to all pennies
cents = round(amount * 100)
print(f"cents: {cents}")
#get the number of whole dollars(//)
dollars = cents // 100
#get remainder(what still needs to be returned)
remainder = cents % 100
#pass remainder into same calc to get quarters, dimes, nickels, pennies
quarters = remainder // 25
remainder = remainder % 25

dimes = remainder // 10
remainder = remainder % 10

nickels = remainder // 5
remainder = remainder % 5

pennies = remainder
#display
print("Coin Breakdown")
print(f"Dollars: {int(dollars)}")
print(f"Quarters: {int(quarters)}")
print(f"Dimes: {int(dimes)}")
print(f"Nickels: {int(nickels)}")
print(f"Pennies: {int(pennies)}")








