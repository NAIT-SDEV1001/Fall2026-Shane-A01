# Write display_game_settings(**settings). Print "Game settings:" followed by each key and value in the format key: value. After the settings, print how many were supplied. Use .items() and len(). With no settings, print the heading and "Setting count: 0".
# Sample calls
# display_game_settings(difficulty="easy", sound=True, lives=3)
# display_game_settings()
# Expected output
# Game settings:
# difficulty: easy
# sound: True
# lives: 3
# Setting count: 3
# Game settings:
# Setting count: 0

def display_game_settings(**settings):
    print("Game Settings:")
    for key, value in settings.items():
        print(f"{key}: {value}")
    print(f"Setting count: {len(settings)}")

display_game_settings()
display_game_settings(difficulty="easy", sound=True, lives=3)
display_game_settings(difficulty="easy", sound=True, lives=3, rating = "pg")

