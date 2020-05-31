# In this project, we will allow the user to input a number
# and then tell the user if that number is prime.
#
# Sample usage: (Ignoring the #'s)
#
# Prime number:
### Input a positive number: 3
### 3 is Prime.
#
# Not prime number:
### Input a positive number: 12
### 12 is not Prime.
#
# Example with bad inputs.
### Input a positive number: -2
### Bad input: -2
### Input a positive number: 3
### 3 is Prime.

# User input - no need to edit this.
x = None
while x == None or x <= 0:
  x = int(input("Input a positive number: "))
  if x <= 0:
    print("Bad input: " + str(x))

# Determine if x is prime and print either:
## print(str(x) + " is Prime.")
## print(str(x) + " is not Prime.")
# TODO(you) - implement this portion.

