import random
import sys
import encription

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

def get_guess(word_length):
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

def play_wordle(secret_word):
    word_length = len(secret_word)
    print("Welcome to Wordle!")
    print(f"Guess the {word_length}-letter word in 6 tries.")

    for attempt in range(1, 7):
        guess = get_guess(word_length)
        if guess == "":
            print("Exiting. Word was", secret_word)
            return False

        feedback = check_guess(secret_word, guess)
        display_feedback(feedback)

        if all(status == 'G' for _, status in feedback):
            print(f"You won in {attempt} tries!")
            return True

        print(f"Try {attempt}/6")

    else:
        print(f"You lost. The word was {secret_word}.")
        return False

def create_custom_wordle():
    custom_word = input("Enter the secret word for your friend: ").strip().upper()
    if not custom_word.isalpha():
        print("Error: Secret word must only contain letters.")
        return None

    encoded_word = encription.encode_base64(custom_word)
    print("\n--- Custom Wordle Created! ---")
    print("Give the following encoded word to your friend:")
    print(f"Encoded Word: {encoded_word}")
    print("-----------------------------------------------\n")
    return encoded_word

def play_custom_wordle():
    encoded_word_input = input("Enter the encoded word: ").strip()
    try:
        secret_word = encription.decode_base64(encoded_word_input)
        if secret_word:
            play_wordle(secret_word)
        else:
            print("Error: Invalid encoded word.")
    except Exception:
        print("Error: Invalid encoded word format.")

def main():
    while True:
        print("\n--- Wordle Game ---")
        print("1. Play Random Wordle")
        print("2. Create Custom Wordle")
        print("3. Play Custom Wordle")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            difficulty = int(input("Choose difficulty (1-5): "))
            if 1 <= difficulty <= 5:
                secret_word = choose_word(difficulty)
                play_wordle(secret_word)
            else:
                print("Invalid difficulty. Please choose between 1 and 5.")
        elif choice == '2':
            create_custom_wordle()
        elif choice == '3':
            play_custom_wordle()
        elif choice == '4':
            print("Exiting Wordle.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
