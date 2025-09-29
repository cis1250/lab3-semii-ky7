#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
for i in range(7):  
    user_inp = int(input("User input: "))
# Validate that the input is a positive integer.
    if user_inp > 0:
        break
    else:
        print("Expected output: Please enter a positive integer.")
else:
    print("Too many invalid attempts. Exiting...")
# Use a for loop to print the Fibonacci sequence up to that many terms
a,b=0,1
print("Expected output:", end=" ")
for i in range(user_inp):
    print(a, end=" ")
    a, b = b, a + b
print()
