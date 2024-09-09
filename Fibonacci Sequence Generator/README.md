# Python Fibonacci Sequence

A Python script that generates the Fibonacci sequence up to a specified number of terms using recursion.

## Features

- Generates the Fibonacci sequence up to a specified number of terms
- Uses a recursive function to calculate the sequence
- Prints the resulting sequence

## Usage

1. Run the `fibonacci.py` script.
2. The script will generate and print the Fibonacci sequence up to 10 terms by default.

## Code Structure

The code consists of a single function `fibonacci(n)` that generates the Fibonacci sequence up to the `n`th term using recursion. Here's how it works:

1. If `n` is less than or equal to 1, the function returns a list containing only 0, as the first Fibonacci number is 0.
2. If `n` is equal to 2, the function returns a list containing the first two Fibonacci numbers: 0 and 1.
3. For all other cases, the function recursively calls itself with `n-1` to get the Fibonacci sequence up to the `n-1`th term.
4. The function then appends the next Fibonacci number to the sequence by summing the last two numbers in the sequence.
5. Finally, the function returns the complete Fibonacci sequence up to the `n`th term.

The `print(fibonacci(10))` statement at the end of the script generates and prints the Fibonacci sequence up to the 10th term.

## Dependencies

- Python 3.12.4 or higher

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a new issue or submit a pull request.
