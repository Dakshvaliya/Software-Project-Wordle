# Wordle Game

Welcome to the Wordle Game project! This command-line implementation of the popular word-guessing game, Wordle, allows you to play with random words or create and share custom Wordle games using encoded secret words.

![Game Screenshot](image.png)

## Features

- **Play Random Wordle**: Select a difficulty level and guess a randomly chosen word.
- **Create Custom Wordle**: Encode a secret word and share it with friends to play.
- **Play Custom Wordle**: Decode and play a custom Wordle game using an encoded secret word.
- **Base64 Encoding/Decoding**: Encode and decode words using Base64 for custom Wordle games.

## Getting Started

### Prerequisites

- Python 3.x
- Custom `encription` library (ensure it's available in your environment)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Dakshvaliya/Software-Project-Wordle.git
    ```

### Usage

Run the game using the following command:

```bash
python main.py
```

Follow the on-screen instructions to play the game.

## Gameplay

1. **Play Random Wordle**:
    - Choose a difficulty level (1-5).
    - Guess the word within 6 attempts.
    - Feedback is provided after each guess:
        - 🟢 Correct letter in the correct position.
        - 🟡 Correct letter in the wrong position.
        - ⬛ Letter not in the word.

2. **Create Custom Wordle**:
    - Enter a secret word.
    - Share the encoded word with friends.

3. **Play Custom Wordle**:
    - Enter the encoded word provided by a friend.
    - Guess the word within 6 attempts.

## Project Structure

- `wordle_game.py`: Main game file containing all the game logic.
- `encription.py`: Custom library for encoding and decoding words (ensure this file is present).
- `words_*.txt`: Text files containing words for each difficulty level.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Inspired by the original Wordle game.
