# In this project, we will allow the user to input a number
# and then tell the user if that number is prime.
#
# Sample usage: (Ignoring the #'s)
#
# Prime number:
### Input a number greater than 1: 3
### 3 is Prime.
#
# Not prime number:
### Input a number greater than 1: 12
### 12 is not Prime.
#
# Example with bad inputs.
### Input a number greater than 1: -2
### Bad input: -2
### Input a number greater than 1: 3
### 3 is Prime.

# User input - no need to edit this.
x = None
while x == None or x <= 1:
  x = int(input("Input a number greater than 1: "))
  if x <= 1:
    print("Bad input: " + str(x))

# Determine if x is prime and print exactly one of:
## print(str(x) + " is Prime.")
## print(str(x) + " is not Prime.")
#
# This should be the ONLY thing you print - you will lose points
# if your solution prints anything else. Feel free to use anything
# else we've learned so far.
# Some hints: Math, Variables, int(..), if/elif/else, while.
#
# TODO(you) - implement this portion.