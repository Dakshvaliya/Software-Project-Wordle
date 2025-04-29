# Importing necessary libraries
import random
import sys
import encription # Custom library

# This chooses a random word for the game based on the difficulty level frm the predetermined word list
def choose_word(difficulty):
    words = [] # Creation of empty array
    word_length = difficulty + 3  # converting the diffulty into a word length
    file_name = f"words_{word_length}.txt"  # defines the file address

    try:
        with open(file_name, "r") as file: # retrives words from the file and adds them to the array
            for line in file: # Loops for each line in the file
                word = line.strip().upper() # converts the everything to uppercase as a precaution
                if len(word) == word_length and word.isalpha(): # makes sure if the word is valid
                    words.append(word) # If it is added it to the array
    # Error handling 
    except FileNotFoundError:
        print(f"Error: '{file_name}' not found.") # displays error if the file is not found and stops the program
        sys.exit()

    if not words:
        print(f"Error: No valid words found in '{file_name}'.") # displays error if there are no valid words and stops the program
        sys.exit()

    return random.choice(words) # returns a random word from the array

# This gets the guess from the user and validates it
def get_guess(word_length):
    while True: # loops until a vaild guess is made
        guess = input(f"Guess the {word_length}-letter word (or exit): ").upper() # Input for the guess and is converted into uppercase
        if guess == "EXIT": # exits if the user types exit
            return ""
        if len(guess) != word_length: # loops if the guess is not the same length as the secert word.
            print(f"Must be {word_length} letters.")
        elif not guess.isalpha(): # loops if the guess contains non-letter characters. Like numbers and symbols
            print("Only letters.")
        else:
            return guess # if everything is correct returns the guess

# This checks the guess against the secret word and returns the feedback
def check_guess(secret_word, guess):
    result = [] # creation of empty array
    for i, letter in enumerate(guess): # loop for each letter in the guess
        if letter == secret_word[i]: # Checks if the letter is in the correct position in the secret word
            result.append((letter, 'G')) # adds the letter and it's status to the array
        elif letter in secret_word: # Checks if the letter is in the secret word but in the wrong position
            result.append((letter, 'Y')) # adds the letter and it's status to the array
        else: # it's no where in the secert word
            result.append((letter, 'B')) # adds the letter and it's status to the array
    return result 

# This displays the feedback to the user
def display_feedback(feedback):
    for letter, status in feedback: # loop for each letter in the feedback
        if status == 'G': # If the status is G / green it will display the letter in green
            print(f"\033[92m{letter}\033[0m", end="") # Uses Unicode to display the letter in green
        elif status == 'Y': # If the status is Y / yellow it will display the letter in yellow
            print(f"\033[93m{letter}\033[0m", end="") # Uses Unicode to display the letter in yellow
        else: # If the status is B / black it will display the letter in grey
            print(f"\033[90m{letter}\033[0m", end="") # Uses Unicode to display the letter in Grey
    print() # Leaves a line after the feedback

# This plays the game 
def play_wordle(secret_word):
    word_length = len(secret_word) # Gets the length of the secret word
    print("Welcome to Wordle!")
    print(f"Guess the {word_length}-letter word in 6 tries.") 
    
    for attempt in range(1, 7): # loop for each attempt
        guess = get_guess(word_length)
        if guess == "": # exits if the user types exit
            print("Exiting. Word was", secret_word)
            return False # Indicates a loose

        feedback = check_guess(secret_word, guess) # Retrives the feedback
        display_feedback(feedback) # displays the feedback 

        if all(status == 'G' for _, status in feedback): # Checks if all the letters are in the correct position
            print(f"You won in {attempt} tries!") # displays the win message
            return True # Indicates a win

        print(f"Try {attempt}/6")

    else:
        print(f"You lost. The word was {secret_word}.") # displays the lose message
        return False # Indicates a loose

# Creation of a Custom Wordle
def create_custom_wordle():
    custom_word = input("Enter the secret word for your friend: ").strip().upper() # takes the word and converts it into a uppercase
    if not custom_word.isalpha(): # Checks if the word is only letters. No numbers, symbols or spaces
        print("Error: Secret word must only contain letters.") # displays error if the word is not only letters
        return None # exits

    encoded_word = encription.encode_base64(custom_word) # encodes the word into a base64 string
    print("\n--- Custom Wordle Created! ---") # displays the encoded word
    print("Give the following encoded word to your friend:")
    print(f"Encoded Word: {encoded_word}")
    print("-----------------------------------------------\n")
    return encoded_word

# Play a custom wordle
def play_custom_wordle():
    encoded_word_input = input("Enter the encoded word: ").strip() 
    try: 
        secret_word = encription.decode_base64(encoded_word_input) 
        if secret_word: # Checks if the word is valid
            play_wordle(secret_word)
        else: # Error handling
            print("Error: Invalid encoded word.")
    except Exception:
        print("Error: Invalid encoded word format.")

# Main function
def main():
    while True:
        print("\n--- Wordle Game ---") # displays the menu
        print("1. Play Random Wordle")
        print("2. Create Custom Wordle")
        print("3. Play Custom Wordle")
        print("4. Exit")

        choice = input("Enter your choice: ") # takes the choice from the user 

        if choice == '1': # plays a random wordle
            difficulty = int(input("Choose difficulty (1-5): "))
            if 1 <= difficulty <= 5: # Checks if the difficulty is valid
                secret_word = choose_word(difficulty)
                play_wordle(secret_word) # plays the game
            else: # Error handling
                print("Invalid difficulty. Please choose between 1 and 5.")
        elif choice == '2': # creates a custom wordle
            create_custom_wordle()
        elif choice == '3': # plays the custom wordle
            play_custom_wordle()
        elif choice == '4': # exits the game
            print("Thanks for playing Wordle.")
            break
        else: # Error handling
            print("Invalid choice. Please try again.")

# Runs the main function
if __name__ == "__main__": 
    main()
