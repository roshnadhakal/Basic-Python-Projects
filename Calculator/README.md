# Python Simple Calculator

A simple command-line calculator built using Python 3.12.4 that performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Features

- Performs basic arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- User-friendly command-line interface
- Handles division by zero gracefully

## Usage

1. Run the `calculator.py` script.
2. The program will display a menu with available operations.
3. Select an operation by entering the corresponding number (1-5):
   - **1**: Add
   - **2**: Subtract
   - **3**: Multiply
   - **4**: Divide
   - **5**: Exit
4. If you choose an operation (1-4), the program will prompt you to enter two numbers.
5. The result of the operation will be displayed.
6. You can continue performing operations until you choose to exit the calculator.

## Code Structure

The code consists of the following functions:

- `add(a, b)`: Returns the sum of `a` and `b`.
- `subtract(a, b)`: Returns the difference between `a` and `b`.
- `multiply(a, b)`: Returns the product of `a` and `b`.
- `divide(a, b)`: Returns the quotient of `a` and `b`, or an error message if division by zero is attempted.
- `calculator()`: The main function that interacts with the user, displays the menu, and processes user input.

The program runs in a loop, allowing users to perform multiple calculations until they choose to exit.

## Dependencies

- Python 3.12.4 or higher

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a new issue or submit a pull request.

