# Python Palindrome Checker

A simple Python script that checks if a given word is a palindrome or not.

## Features

- Takes user input for a word
- Checks if the word is the same forwards and backwards
- Prints whether the word is a palindrome or not

## Usage

1. Run the `palindrome_checker.py` script.
2. Enter a word when prompted.
3. The script will check if the word is a palindrome and display the result.

## Code Structure

The code consists of the following steps:

1. The user is prompted to enter a word using the `input()` function and storing it in the `word` variable.
2. The `reverse_word` variable is created by reversing the `word` using string slicing with the step `-1` (i.e., `[::-1]`).
3. An `if` statement checks if the `reverse_word` is equal to the original `word`.
   - If they are equal, it means the word is a palindrome, and a message is printed indicating that the word is a palindrome.
   - If they are not equal, it means the word is not a palindrome, and a message is printed indicating that the word is not a palindrome.

## Dependencies

- Python 3.12.4 or higher

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a new issue or submit a pull request.

