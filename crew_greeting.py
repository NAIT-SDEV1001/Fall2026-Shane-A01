# Question 1 - Space crew greeting

# Use the default role when the caller supplies only a name.
def display_greeting(name, role="Explorer"):
    print(f"Welcome aboard, {name}! Role: {role}")


# Mainline: demonstrate the default role and a custom role.
display_greeting("Mia")

display_greeting("Noah", "Pilot")
