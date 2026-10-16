# A while loop repeats an indented block while its condition is true.
# The condition is checked BEFORE each iteration, so it may run zero times.
# Useful when the number of repetitions is not known in advance.
# For a loop intended to finish, something must eventually make
# the condition false or execute break.

#ask the user how high to count 
number = int(input("What number do you want to count to? "))

counter = 1

while counter <= number: #keep looping while counter <= number. checks this condition BEFORE entering the loop
    print(f"Number: {counter}")
    counter += 1

#Add up numbers entered by the user until they enter "done"
#Using a True loop

print("Enter numbers to add. Type 'done'  to finish")

sum = 0

while True: # an endless loop, unless break
    value = input("Enter a number: ")
    #Check if done was entered and break
    if value.lower() == "done":
        break#breaks out of loop
    #add number to sum
    sum += int(value)

#print the sum
print(f"Sum = {sum}")

#using a Boolean flag
keep_going = True

while keep_going:
    answer = input("Keep going? (y/n): ")
    if answer.lower() == "n":
        keep_going = False

print("End of Loop")


















