#elif
movie_name = input("Enter a movie name: ")
if movie_name.upper() == "STAR WARS" or movie_name.upper() == "JURASSIC PARK"              :
    print("Awesome!")
elif movie_name.upper() == "JONES":
    print("Cool!")
elif movie_name.upper() == "SHREK":
    print("Donkey")
else:
    print("Unknown")

#match case
match movie_name.upper():
    case "STAR WARS" | "JURASSIC PARK":
        print("Awesome!")
    case "JONES":
        print("Cool!")
    case "SHREK":
        print("Donkey")
    case _:
        print("Unknown")



