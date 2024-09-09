# Python Scissors, Paper, Rock Game

A simple implementation of the classic Scissors, Paper, Rock game using Python 3.12.4.

## Features

- Player can choose between scissors, paper, or rock
- Computer randomly selects its choice
- Game determines the winner based on the classic rules
- Allows the player to play again after each round

## Usage

1. Run the `scissors_paper_rock.py` script.
2. The game will prompt you to enter your choice (scissors, paper, or rock).
3. The computer will randomly select its choice.
4. The winner will be determined based on the classic Scissors, Paper, Rock rules.
5. After each round, the game will ask if you want to play again.
6. Enter "yes" to play again or "no" to exit the game.

## Code Structure

The game is implemented using a single function `game()` that handles the entire game logic. Here's how it works:

1. The function defines a list `choices` containing the possible choices: "scissors", "paper", and "rock".
2. The computer randomly selects its choice using `random.choice(choices)`.
3. The player is prompted to enter their choice, and the input is converted to lowercase for case-insensitivity.
4. The player's input is validated to ensure it matches one of the valid choices.
5. The game compares the player's choice and the computer's choice to determine the winner based on the classic rules.
6. The result is printed to the console.
7. The player is prompted to play again, and the input is validated to ensure it's either "yes" or "no".
8. If the player chooses "yes", the `game()` function is called recursively to restart the game.
9. If the player chooses "no" or any other invalid input, the game prints a farewell message and exits.

## Dependencies

- Python 3.12.4 or higher
- `random` module (built-in)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a new issue or submit a pull request.
