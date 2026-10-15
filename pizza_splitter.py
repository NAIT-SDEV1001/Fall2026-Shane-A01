print("Question 1 - Pizza Splitter")

try:
    cost = float(input("Enter the total pizza cost: "))
    people = int(input("Enter the number of people: "))
    cost_per_person = cost / people
except ValueError:
    print("Enter a numeric cost and a whole number of people.")
except ZeroDivisionError:
    print("You cannot split the cost among zero people.")
else:#runs only if no exceptions
     print(f"Cost per person: ${cost_per_person:.2f}")

print("Have a groovy day!")


