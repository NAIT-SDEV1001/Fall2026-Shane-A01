#add 0.1 + 0.2
answer = 0.1 +0.2
print(answer)
# prints 0.30000000000000004
#issue is the decmial places are stored in binary. values like .1, .2 cannot be stored perfectly in binary

amount = 1.15
print(f"calculation: {amount * 100}")
print (f"Convert to int: {int(amount * 100)}")
print(f"using round(): {round(amount * 100)}")

#another proof
print(0.1 + 0.2)
print((0.1 + 0.2) == 0.3)

