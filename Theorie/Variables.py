print("***************************")
# Can assign multiple values to multiples variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
print("***************************")
# Can assign the same value to multiple variables
x = y = z = "Berry"
print(x)
print(y)
print(z)
print("***************************")
# Can unpack a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print("***************************")
# Global variables
# Create a global variable outside a function
# Create a variable with the same name but local inside the function
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 
print("***************************")
# To use the global variable inside a function, use global keyword

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 
print("***************************")