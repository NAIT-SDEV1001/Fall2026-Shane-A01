#tuple of vowels
vowels = ("a","e","i","o","u")
#create a total variable
total = 0
# get the word from the user
word = input("Enter a word: ")

#loop through word (each char)
#check if the letter is in the tuple
for character in word:
    #if character.lower() in vowels:
#OR 
    if character.lower() in "aeiou":
        total += 1
print(f"There are {total} vowels in {word}")
    
