user_number = int(input("Enter a number to sum the squares: "))
sum = 0

for number in range (1,user_number + 1):
    sum  += number ** 2#same as sum = sum + number ** 2

print(f"The sum of squares is: {sum}")