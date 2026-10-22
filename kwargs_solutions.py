# Solutions for kwargs.py practice: Questions 3 and 4.

# Question 3 - Game settings
# **settings collects keyword arguments into a dictionary.
def display_game_settings(**settings):
    print("Game settings:")
    for key, value in settings.items():
        print(f"{key}: {value}")
    print(f"Setting count: {len(settings)}")

display_game_settings(difficulty="easy", sound=True, lives=3)
display_game_settings()


# Question 4 - Fundraiser donations
def calculate_donations(**donations):
    total = 0
    # Unpack each dictionary entry into a donor name and an amount.
    for name, amount in donations.items():
        print(f"{name}: ${amount:.2f}")
        total += amount
    return total


print("Question 3 - Game settings")
display_game_settings(difficulty="easy", sound=True, lives=3)
display_game_settings()
print("\nQuestion 4 - Fundraiser donations")
total = calculate_donations(Alex=10, Sam=7.50, Riley=12.25)
print(f"Total raised: ${total:.2f}")
# Check the empty case as well.
total = calculate_donations()
print(f"Total raised with no donations: ${total:.2f}")
