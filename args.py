# *args is a parameter that allows functions to accept ANY number of positional arguments
# arguments passed into an arg are stored in a tuple
# args is common name for this parameter. The * is what makes it an arg

def print_numbers(*numbers):#accept the arguments into a tuple called numbers
    #print out each number in numbers
    for number in numbers:
        print(number)

print_numbers (1,3,5,22,66,3434,1223,765,232,11543,5,142,23,3274)





