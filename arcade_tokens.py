# Question 3 - Refactoring the arcade token program

def display_welcome():
    print("Welcome to Pixel Palace!")


# Keep input and output separate from this calculation function.
def calculate_tokens(packs, tokens_per_pack=10):
    return packs * tokens_per_pack


def display_summary(player_name, tokens):
    print(f"Player: {player_name}")
    print(f"Tokens: {tokens}")


# Mainline: coordinate the input, calculation, and output.
display_welcome()
player_name = input("Player name: ")
packs = int(input("Number of token packs: "))
tokens = calculate_tokens(packs)
display_summary(player_name, tokens)

# Bonus token day: replace the calculation above with this call.
tokens = calculate_tokens(packs, 15)
