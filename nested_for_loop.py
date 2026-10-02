# Print 3 rows X 4 seats
for row in range(1,4):
    for seat in range(1,5):
        name = input("Enter your name: ")
        print(f"Row {row}, Seat {seat} is purchased by {name}")

#ask the user for number of rows and columns. build a rectangle of those dimensions with *
rows = int(input("Number of rows: "))
columns = int(input("Number of columns: "))

for row in range(0,rows):
    for column in range(0,columns):
        print("*",end ="")
    print()    
    




 
