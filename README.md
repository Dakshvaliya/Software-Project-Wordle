# Wordle Game

Welcome to the Wordle Game! This is a command-line version of the popular word-guessing game Wordle. The game allows you to choose from five difficulty levels, each with increasing word lengths.

## Features

- Five difficulty levels with word lengths ranging from 4 to 8 letters.
- Feedback on each guess with color-coded letters.
- Option to play multiple rounds.

## Requirements

- Python 3.
- Word list files: `words_4.txt`, `words_5.txt`, `words_6.txt`, `words_7.txt`, `words_8.txt`

## Setup

1. **Clone the Repository** (if applicable) or download the script.
2. **Prepare Word List Files**: Ensure you have the word list files (`words_4.txt`, `words_5.txt`, `words_6.txt`, `words_7.txt`, `words_8.txt`) in the same directory as the script. Each file should contain words of the specified length, one word per line.
3. **Run the Game**: Execute the script using Python.

```bash
python main.py
```

## How to Play

1. **Choose Difficulty**: When prompted, enter a difficulty level between 1 and 5. This determines the length of the word you need to guess (4 to 8 letters).
2. **Guess the Word**: Enter your guess for the word. The game will provide feedback on each letter:
   - Green: Letter is correct and in the correct position.
   - Yellow: Letter is correct but in the wrong position.
   - Gray: Letter is not in the word.
3. **Win or Lose**: You have 6 attempts to guess the word. If you guess correctly within 6 tries, you win. Otherwise, the game reveals the word, and you lose.
4. **Play Again**: After each round, you can choose to play again or exit the game.

## Files

- `wordle_game.py`: The main game script.
- `words_4.txt`: List of 4-letter words.
- `words_5.txt`: List of 5-letter words.
- `words_6.txt`: List of 6-letter words.
- `words_7.txt`: List of 7-letter words.
- `words_8.txt`: List of 8-letter words.

## Notes

- Ensure the word list files are correctly formatted with one word per line and no extra characters.
- The game is case-insensitive, but guesses are converted to uppercase for consistency.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests. Any contributions are welcome!

---

Enjoy playing Wordle! If you have any questions or issues, please open an issue in the repository.
