import random
import sys

def choose_word():
    words = []
    try:
        with open("words.txt", "r") as file:
            for line in file:
                word = line.strip().upper()
                if len(word) == 5 and word.isalpha():
                    words.append(word)
    except FileNotFoundError:
        print("Error: 'words.txt' not found.")
        sys.exit() 
    
    if not words:
        print("Error: No valid words found in 'words.txt'.")
        sys.exit()
    return random.choice(words)

def get_guess():
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
        secret_word = choose_word()
        print("Welcome to Wordle!")
        print("Guess the word in 6 tries.")

        for attempt in range(1, 7):
            guess = get_guess()
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
