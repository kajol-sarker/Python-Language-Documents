#Python Number Guessing Game

import random

RandomNumber = random.randrange(1,500)
# print("And the Random Number is:", RandomNumber)       #this line is for when we want to match the user number = random number
user = int(input("Guess the number: "))

if user > RandomNumber:
    print("And the Random Number is:", RandomNumber)
    print("So The Number is too high")
elif user < RandomNumber:
    print("And the Random Number is:", RandomNumber)
    print("So The Number is too low")
else:
    print("And the Random Number is:", RandomNumber)
    print("The number is equal.")

