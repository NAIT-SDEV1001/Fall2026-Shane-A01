print("\n1. Rocket Countdown")
starting_number = int(input("Enter a starting number: "))

while starting_number < 1:
    print(f"{starting_number} is invalid. Please enter a positive number.")
    starting_number = int(input("Enter a starting number: "))

count = starting_number #sometimes it is a good idea to rename the variable to something more appropriatte for the rest of the code

while count >= 1:
    print(count)
    count -= 1

print("Blast Off!")




