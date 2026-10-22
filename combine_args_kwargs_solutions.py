# Solutions for combine_args_kwargs.py practice: Questions 5 and 6.

# Question 5 - Movie night
# Positional arguments go into movies; keyword arguments go into details.
def movie_night(*movies, **details):
    print("Movies:")
    if len(movies) == 0:
        print("No movies selected.")
    for movie in movies:
        print("-", movie)
    print("Details:")
    if len(details) == 0:
        print("No details supplied.")
    for key, value in details.items():
        print(f"{key}: {value}")


# Question 6 - Build a robot
def build_robot(*parts, **features):
    print("Robot parts:")
    for part in parts:
        print("-", part)
    print("Features:")
    for key, value in features.items():
        print(f"{key}: {value}")
    # len() works with both the tuple and the dictionary.
    print(f"Part count: {len(parts)}")
    print(f"Feature count: {len(features)}")


print("Question 5 - Movie night")
movie_night("Shrek", "Toy Story", snack="Popcorn", start="7 PM")
print("\nEmpty movie night:")
movie_night()
print("\nQuestion 6 - Build a robot")
build_robot("Wheels", "Claw", "Camera", name="Bolt", colour="Blue")
print("\nEmpty robot:")
build_robot()
