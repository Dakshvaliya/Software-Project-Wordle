import random
import sys

def choose_word(difficulty):
    words = []
    word_length = difficulty + 3
    file_name = f"words_{word_length}.txt"

    try:
        with open(file_name, "r") as file:
            for line in file:
                word = line.strip().upper()
                if len(word) == word_length and word.isalpha():
                    words.append(word)
    except FileNotFoundError:
        print(f"Error: '{file_name}' not found.")
        sys.exit()

    if not words:
        print(f"Error: No valid words found in '{file_name}'.")
        sys.exit()

    return random.choice(words)

def get_guess(difficulty):
    word_length = difficulty + 3
    while True:
        guess = input(f"Guess the {word_length}-letter word (or exit): ").upper()
        if guess == "EXIT":
            return ""
        if len(guess) != word_length:
            print(f"Must be {word_length} letters.")
        elif not guess.isalpha():
            print("Only letters.")
        else:
            return guess

def check_guess(secret_word, guess):
    result = []
    for i, letter in enumerate(guess):
        if letter == secret_word[i]:
            result.append((letter, 'G'))
        elif letter in secret_word:
            result.append((letter, 'Y'))
        else:
            result.append((letter, 'B'))
    return result

def display_feedback(feedback):
    for letter, status in feedback:
        if status == 'G':
            print(f"\033[92m{letter}\033[0m", end="")
        elif status == 'Y':
            print(f"\033[93m{letter}\033[0m", end="")
        else:
            print(f"\033[90m{letter}\033[0m", end="")
    print()

def play_wordle():
    while True:
        difficulty = int(input("Choose difficulty (1-5): "))
        if difficulty < 1 or difficulty > 5:
            print("Invalid difficulty. Please choose between 1 and 5.")
            continue

        secret_word = choose_word(difficulty)
        print("Welcome to Wordle!")
        print("Guess the word in 6 tries.")

        for attempt in range(1, 7):
            guess = get_guess(difficulty)
            if guess == "":
                print("Exiting. Word was", secret_word)
                break

            feedback = check_guess(secret_word, guess)
            display_feedback(feedback)

            if all(status == 'G' for _, status in feedback):
                print(f"You won in {attempt} tries!")
                break

            print(f"Try {attempt}/6")

        else:
            print(f"You lost. The word was {secret_word}.")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

play_wordle()
