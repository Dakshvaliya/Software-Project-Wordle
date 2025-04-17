import random

def choose_word():
    """Random Word list I made in 10 seconds, I know it's just fruits."""
    words = ["apple", "mango", "grape", "lemon", "melon", "berry", "peach"]
    return random.choice(words).upper()

def get_guess():
    """Get and check user's guess."""
    while True:
        guess = input("Guess the 5-letter word (or exit): ").upper()
        if guess == "EXIT":
            return ""
        if len(guess) != 5:
            print("Must be 5 letters.")
        elif not guess.isalpha():
            print("Only letters.")
        else:
            return guess

def check_guess(secret_word, guess):
    """Check guess and give feedback."""
    result = []
    for i, letter in enumerate(guess):
        if letter == secret_word[i]:
            result.append((letter, 'G'))  # Green
        elif letter in secret_word:
            result.append((letter, 'Y'))  # Yellow
        else:
            result.append((letter, 'B'))  # Black
    return result

def display_feedback(feedback):
    """Show feedback to user."""
    for letter, status in feedback:
        if status == 'G':
            print(f"\033[92m{letter}\033[0m", end="")
        elif status == 'Y':
            print(f"\033[93m{letter}\033[0m", end="")
        else:
            print(f"\033[90m{letter}\033[0m", end="")
    print()

def play_wordle():
    """Play the game."""
    secret_word = choose_word()
    print("Welcome to Wordle!")
    print("Guess the word in 6 tries.")

    for attempt in range(1, 7):
        guess = get_guess()
        if guess == "":
            print("Exiting. Word was", secret_word)
            return

        feedback = check_guess(secret_word, guess)
        display_feedback(feedback)

        if all(status == 'G' for _, status in feedback):
            print(f"You won in {attempt} tries!")
            return

        print(f"Try {attempt}/6")

    print(f"You lost. The word was {secret_word}.")

play_wordle()
