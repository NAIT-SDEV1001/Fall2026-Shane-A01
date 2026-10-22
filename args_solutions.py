# Solutions for args.py practice: Questions 1 and 2.

# Question 1 - Snack roll call
# *snacks collects positional arguments into a tuple.
def display_snacks(*snacks):
    if len(snacks) == 0:
        print("No snacks packed!")
    else:
        for snack in snacks:
            print("-", snack)
        print(f"Snack count: {len(snacks)}")

display_snacks("Popcorn", "Pretzels", "Cookies")
display_snacks()



# Question 2 - Arcade points
def calculate_points(*scores):
    total = 0
    for score in scores:
        total += score
    # With no scores, the loop is skipped and total remains 0.
    return total



print("Question 1 - Snack roll call")
display_snacks("Popcorn", "Pretzels", "Cookies")
display_snacks()


print("\nQuestion 2 - Arcade points")
print(calculate_points(10, 25, 15))
print(calculate_points(100, 50))
print(calculate_points())
