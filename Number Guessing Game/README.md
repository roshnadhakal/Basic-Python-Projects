# Python Guessing Game

A simple number guessing game built using Python 3.12.4.

## Features

- The game selects a random number between 1 and 100 (or any other range) for the user to guess.
- The user is prompted to enter a guess.
- If the user's guess is incorrect, the game provides a hint (higher or lower) and prompts the user to guess again.
- The game continues until the user correctly guesses the number.
- When the user guesses correctly, the game congratulates the user and displays the number.

## Usage

1. Run the `guessing_game.py` script.
2. The game will prompt you to enter a guess.
3. Enter a number and press Enter.
4. If your guess is incorrect, the game will provide a hint and prompt you to guess again.
5. Keep guessing until you enter the correct number.
6. Once you guess correctly, the game will congratulate you and display the number.

## Code Structure

The code consists of the following elements:

1. `gameNum`: This variable holds the number to be guessed by the user. In the provided code, it is set to 70, but you can modify it to generate a random number within a specific range.

2. `userNum`: This variable stores the user's guess. It is initialized with the user's first input using `int(input("Guess the number: "))`.

3. The `while` loop continues until the user correctly guesses the number (`gameNum`). Inside the loop:
   - The user's guess is compared to the correct number using the `!=` operator.
   - If the guess is incorrect, the user is prompted to guess again using `int(input("You entered wrong number. Guess Again! : "))`.

4. When the user correctly guesses the number, the loop terminates, and the congratulatory message is displayed using `print("Congratulation! you entered correct number", gameNum)`.

## Dependencies

- Python 3.12.4 or higher

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a new issue or submit a pull request.
