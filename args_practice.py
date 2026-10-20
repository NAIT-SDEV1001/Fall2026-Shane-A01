# Question 1 Snack roll call
# Write display_snacks(*snacks). Print each snack on its own line, starting with a dash. Then print the number of snacks. If no snacks are supplied, print only "No snacks packed!". Use a loop and len().
# Sample calls
# display_snacks("Popcorn", "Pretzels", "Cookies")
# display_snacks()
# Expected output
# - Popcorn
# - Pretzels
# - Cookies
# Snack count: 3
# No snacks packed!

def display_snacks(*snacks):
    if len(snacks) == 0:
        print("No snacks packed!")
    else:
        for snack in snacks:
            print(f"- {snack}")
        print(f"Snack count: {len(snacks)}")

# display_snacks()
display_snacks("Popcorn", "Pretzels", "Cookies")
