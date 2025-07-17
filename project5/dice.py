#Python Dice Rolling Simulator Game

import random

dicerolling =  True

while dicerolling:
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}")
    PlayAgain = input("Do you wanna play again the rol?: ")
    if PlayAgain == "Yes":
        continue
    else:
        print("game over")
        break