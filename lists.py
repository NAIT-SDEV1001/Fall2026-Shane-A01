#list is a collection of values
#each value in a list is stored in an element
#can hold different datatypes (including other lists!)

colors = ["red", "blue", "green", "yellow"]

#display the list
print(colors)

#access elements by a zero based index
print(colors[1])

#from end list
print(colors[-2])

colors[2] = "purple"
print(colors)

#using an index not in the list is an error
# print(colors[4])

#length of a list
print(len(colors))

#slicing
#gets values from a range in the list
letters = ["a","b","c","d","e"]
print(f"First three letters: {letters[0:3]}")
#with slicing the upper boundary is not inclusive

#if you start at the first index it can be omitted
print(f"First three letters: {letters[:3]}")

#if you start at the end you can omit as well
print(f"Last 2 letters: {letters[-2:]}")






