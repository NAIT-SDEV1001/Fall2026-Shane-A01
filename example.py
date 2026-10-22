def display_grades (name,grade):
    print(f"{name}: {grade}")

grades = [("Bob",40),("Sue",90),("Joe",76)]

for student in grades:
    display_grades(*student)
