#Python Hangman Game

# Python Hangman Game

word = "Kajol"
chances = 7
GuessAdd = []
done = False

while not done:
    # Show guessed letters or underscores
    for letter in word:
        if letter.lower() in GuessAdd:
            print(letter, end=' ')
        else:
            print("_", end=' ')
    print()  # new line

    # Take user input
    Myguess = input(f"Your chances are {chances}. Guess a letter: ").lower()
    GuessAdd.append(Myguess)

    # Decrease chance if wrong
    if Myguess not in word.lower():
        chances -= 1
        if chances == 0:
            break

    # Check if all letters are guessed
    done = True
    for letter in word:
        if letter.lower() not in GuessAdd:
            done = False
            break

# Final result
if done:
    print(f"✅ Yes, you won the game! The word is '{word}'.")
else:
    print(f"❌ You lost the game. The correct word was '{word}'.")
