#!/usr/bin/python3

# Import the random module to generate random numbers
import random

# Generate a random signed number between -10 and 10 (inclusive)
number = random.randint(-10, 10)

# Check whether the number is positive, zero, or negative and print the result
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
