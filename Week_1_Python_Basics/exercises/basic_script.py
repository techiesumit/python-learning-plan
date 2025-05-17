print ( "This is script.py file" )

x=2
if x == 1:
    print("x is 1")
else:
    print("x is not 1")

mystring = "This is how to create a string in Python"
print(mystring)
# List are like arrays in other languages
mylist = [1,2,3,4,5]
mylist.append(6)
mylist.insert(0, 7)
print("My List is " ,mylist)
print(mylist[6])
# Tuples are immutable lists
mytuple = (1,2,3,4,5)
print(mytuple[0])
# Dictionaries are like HashMap Or Map objects in other languages
mydictionary = {"one": 1, "two": 2, "three": 3} 
print(mydictionary["two"])

# Operators in  Python
sum = 1 + 2
print("Sum is ", sum)
sub = 1 - 2
print("Subtraction is ", sub)
mul = 1 * 2
print("Multiplication is ", mul)
div = 1 / 2
print("Division is ", div)
mod = 5 % 3
print("Modulus/ Reminder  is ", mod)
pow = 2 ** 3
print("Power is ", pow)

#Python supports concatenating strings using the addition operator
print("Hello" + " " +"Sumit")
#Python supports repeating strings using the multiplication operator
print("Hello " * 3)

# + operator can be used to concatenate lists
print([1, 2, 3] + [4, 5, 6])
# * operator can be used to repeat lists
print([1, 2, 3] * 3)

# Python supports string formatting using the format() method
name = "Sumit"
print("Hello, {}".format(name))
# Python supports string formatting using f-strings (Python 3.6 and later)
name = "Sumit"
print(f"Hello, {name}")
# Python supports string interpolation using the % operator
name = "Sumit"
print("Hello, %s" % name)

# Create empty Object
myemptyobject = object()
print(myemptyobject)
# Create empty list
myemptylist = []
print(myemptylist)
# Python supports forming new lists with a repeating sequence using the multiplication operator:
print([1,2,3] * 8)

#Variabe Substitution use %s for string, %d for integer
name = "Sumit"  
age = 49
state="IA"
country = "USA"
print("My name is %s, I am %d years old and I live in %s ,%s" % (name, age, state,country))

#Check the type of variable
print(type(name))
print(type(age))
del age
#print(age)

#assign nothing to  variable
name = None
print(name)
#Python supports the use of the in operator to check if a value is in a l

data = ("John", " Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

