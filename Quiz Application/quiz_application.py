# Quiz Application

# Dictionary of questions and their correct answers
questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the largest ocean on Earth?": "Pacific",
    "What is the square root of 16?": "4"
}

# Function to run the quiz
def run_quiz():
    score = 0  # Initialize the score to 0
    
    # Loop through each question and correct answer in the dictionary
    for question, correct_answer in questions.items():
        # Ask the user for their answer
        user_answer = input(question + " ")
        
        # Check if the user's answer matches the correct answer (case-insensitive)
        if user_answer.lower() == correct_answer.lower():
            score += 1  # Increment score if the answer is correct
            print("Correct!")  # Inform the user they got it right
        else:
            # Inform the user they got it wrong and display the correct answer
            print(f"Wrong! The correct answer is {correct_answer}.")
    
    # After the quiz, display the user's final score
    print(f"Your final score is {score}/{len(questions)}.")

# Start the quiz by calling the run_quiz function
run_quiz()
