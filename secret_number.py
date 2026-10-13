print("Guess the Secret Number")
secret_number = 17
attempts = 0
guess_input = input("Guess the secret number (q to quit): ")

# Challenge: check for q before conversion so quitting is not an attempt.
while guess_input.lower() != "q":
    guess = int(guess_input)
    attempts += 1

    if guess == secret_number:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Too low!")

    guess_input = input("Guess the secret number (q to quit): ")

if guess_input.lower() == "q":
    print(f"You quit after {attempts} attempts.")

