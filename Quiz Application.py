#Quiz Application

questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the largest ocean on Earth?": "Pacific",
    "What is the square root of 16?": "4"
}

def run_quiz():
    score = 0
    for question, correct_answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == correct_answer.lower():
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
    print(f"Your final score is {score}/{len(questions)}.")

run_quiz()