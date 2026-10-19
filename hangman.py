import random

words = ["PYTHON", "COMPUTER", "PROGRAM", "STUDENT", "GITHUB"]

secret_word = random.choice(words)
guessed_letters = set()
wrong_guesses = 0
max_attempts = 6

stages = [
    """
     +---+
     |   |
         |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =======
    """
]

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the hidden word!")
print("You have 6 incorrect attempts.")

while wrong_guesses < max_attempts:
    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print("\nWord:", display_word)
    print("Incorrect attempts:", wrong_guesses)
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print(stages[wrong_guesses])

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You won!")
        break

    guess = input("Enter one letter: ").strip().upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter from A to Z.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try another.")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print(stages[max_attempts])
    print("Game over! You lost.")
    print("The correct word was:", secret_word)

print("\nThanks for playing!")