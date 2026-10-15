# Display the snacks numbered 1 through 4, then ask the user to choose one.
# snacks = ["Popcorn", "Pretzels", "Cookies", "Nachos"]
# •	Convert the choice to an integer.
# •	Use raise ValueError(...) if the choice is less than 1.
# •	Access the selected snack using snacks[choice - 1].
# •	Catch ValueError for invalid integer input or choices below 1.
# •	Catch IndexError for choices above 4.
# •	Use else to display the selected snack.
# Try these inputs: 2, banana, 0, and 5. Run the program separately for each input.

print("Question 2 - Snack Selector")
snacks = ["Popcorn", "Pretzels", "Cookies", "Nachos"]
for index, snack in enumerate(snacks, start=1):
    print(f"{index}. {snack}")

try:
    choice = int(input("Choose a snack 1-4: "))
    if choice < 1:
        raise ValueError("Your choice must be at least 1")
    selected_snack = snacks[choice - 1]
except ValueError as error_message:
    print(f"Invalid choice: {error_message}")
except IndexError:   
    print("There is no snack with that number. Choose 1-4")
else: 
    print(f"You selected {selected_snack}")

#seperate ValueError message for < 1 and cast error
print("Question 2 - Snack Selector")
snacks = ["Popcorn", "Pretzels", "Cookies", "Nachos"]
for index, snack in enumerate(snacks, start=1):
    print(f"{index}. {snack}")
try:
    choice = int(input("Choose a snack 1-4: "))    
    
except ValueError:
    print(f"Enter an integer")
else: 
    try:
        if choice < 1:
            raise ValueError ("Your choice must be at least 1")                   
        selected_snack = snacks[choice - 1] 
    except ValueError as error_message:
        print(f"Invalid choice: {error_message}")
    except IndexError:
        print("There is no snack with that number. Choose 1-4")
    else:
        print(f"You selected {selected_snack}")

        