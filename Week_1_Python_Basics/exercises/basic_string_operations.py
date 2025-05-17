letsplaywithStrings = "Let's play with strings"
print(letsplaywithStrings)
# This is how to put single quotes in a string
letsplaywithStrings = 'Let\'s play with strings'
print(letsplaywithStrings)

# This is how to put double quotes in a string
letsplaywithStrings = "Let\"s play with strings"
print(letsplaywithStrings)

# find the first index  of a string
mystring = "This is how to create a string in Python"  
print(mystring.find("string"))
 # find the index of character in a string
mystring = "This is how to create a string in Python"
print(mystring.index("s"))
# find the last index of a string
mystring = "This is how to create a string in Python"   
print(mystring.rfind("s"))
# Total number of occurrences of a string
mystring = "This is how to create a string in Python"
print(mystring.count("t"))
# Upper Case is different than lower case
print(mystring.count("T"))
# print the  lentght of string
print(len(mystring))
# replace a string with another string
mystring = "This is how to create a string in Python"
print(mystring.replace("string", "new string"))
# Slice and dice a  string
mystring = "This is how to create a string in Python"   
print(mystring[4:20])
#Slice and dice and skip step
mystring = "This is how to slice and dice a string in Python"
print(mystring[4:20:2])

# Logical Operators
# Logical operators are used to combine conditional statements
print(1 == 1 and 2 == 2)
# Greater than
print(1 > 2)
# Less than
print(1 < 2)
# Greater than or equal to
print(1 >= 2)
# and and Or and Not
print(1 < 2 and 2 < 3)  
print(1 < 2 or 2 < 3)
print(not(1 < 2 and 2 < 3))
# Boolean
print(True)
print(False)    
#in operator
mystring = "This is how to create a string in Python"   
print("string" in mystring)
# not in operator   
print("string" not in mystring)
# is operator
mystring = "This is how to create a string in Python"
print(mystring is mystring)
# is not operator
print(mystring is not mystring)

# if elif else
if 1 < 2:
    print("1 is less than 2")
    if 2 < 3:
        print("2 is less than 3")
    else:
        print("2 is not less than 3")
elif 1 > 2:
    print("1 is greater than 2")    
else:
    print("1 is not less than 2 and 1 is not greater than 2")

    #Loops
# for loop
for i in range(1, 10):
    print(i)
# while loop
i = 1
while i < 10:
    print(i)
    i += 1
    if i == 5:
        break
# continue
for i in range(1, 10):
    if i == 5:
        continue
    print(i)
# pass
for i in range(1, 10):
    if i == 5:
        pass
    print(i)
# for loop with else
for i in range(1, 10):
    print(i)
    if i == 5:
        break
else:
    print("Loop completed")


primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)