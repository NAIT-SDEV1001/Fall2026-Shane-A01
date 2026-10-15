# Game Score Average
# Repeatedly ask for a whole-number game score. Entering -1 ends input.
# •	Catch ValueError and ask again if the input is not an integer.
# •	Use raise ValueError(...) if the score is outside 0 through 100, allowing -1 to quit.
# •	Only include valid scores in the total and count. Do not include -1.
# •	After the loop, calculate the average.
# •	Catch ZeroDivisionError if no scores were entered.
# •	Use else to display the average to two decimal places.
# Try these inputs: hello, -5, 101, 80, 90, and -1 in that order. The average should be 85.00. Run it again and enter -1 immediately.
# Optional challenge
# Count how many invalid entries the user makes in Question 3 and display that count at the end. Do not count -1 as invalid. The suggested sequence contains three invalid entries.
print("Question 3 - Game Score Average")
total = 0
count = 0
invalid_count = 0  # Optional challenge

while True:
    try:
        score = int(input("Enter a score from 0 through 100 (-1 to quit): "))
        if score != -1 and (score < 0 or score > 100):#could also check <-1 . However, breaking out the clear conditions is good
            raise ValueError("Scores must be from 0 through 100.")
    except ValueError as error_message:
        invalid_count += 1
        print(f"Invalid score: {error_message}")
        continue

    if score == -1:
        break
    total += score
    count += 1

try:
    average = total / count
except ZeroDivisionError:
    print("No scores were entered, so there is no average.")
else:
    print(f"Average score: {average:.2f}")

#Seperate try blocks for getting score value
while True:
    try:
        score = int(input("Enter a score from 0 through 100 (-1 to quit): "))
    except ValueError:
        invalid_count += 1
        print("Invalid score: Enter a whole number.")
        continue

    if score == -1:
        break

    try:
        if score < 0 or score > 100:
            raise ValueError("Scores must be from 0 through 100.")
    except ValueError as error_message:
        invalid_count += 1
        print(f"Invalid score: {error_message}")
        continue

    total += score
    count += 1