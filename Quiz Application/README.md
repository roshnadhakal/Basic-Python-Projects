# Quiz Application

## Description

This is a simple quiz application built using Python. It presents a series of questions to the user and keeps track of their score based on the correct answers provided.

## Features

- Stores questions and their corresponding correct answers in a dictionary
- Allows the user to input their answers for each question
- Checks if the user's answer matches the correct answer (case-insensitive)
- Increments the user's score for each correct answer
- Displays the user's final score at the end of the quiz

## Usage

1. Run the `quiz_app.py` script.
2. The quiz will start, and the first question will be displayed.
3. Enter your answer for each question and press Enter.
4. The application will check if your answer is correct and provide feedback.
5. After answering all the questions, your final score will be displayed.

## Code Structure

The code is organized into a single Python file, `quiz_app.py`, which contains the following components:

1. **questions** dictionary: Stores the questions and their corresponding correct answers.
2. **run_quiz()** function: Manages the flow of the quiz, including:
   - Initializing the score to 0
   - Looping through each question and correct answer in the dictionary
   - Asking the user for their answer
   - Checking if the user's answer matches the correct answer (case-insensitive)
   - Incrementing the score if the answer is correct
   - Providing feedback to the user based on the correctness of their answer
   - Displaying the user's final score at the end of the quiz

The `run_quiz()` function is called to start the quiz.

## Dependencies

- Python 3.12.4 or higher

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a new issue or submit a pull request.
