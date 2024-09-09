import random;

# Define a function to play the  Scissors, Paper, Rock, game
def game():
    choices = ["scissors", "paper", "rock"]
  
     # Computer randomly selects its choice
    computerChoice = random.choice(choices)
    userChoice = input("Please Enter Your Choice (scissors, paper, or rock): ").lower()
  
    # Validate the user's input
    while userChoice not in choices:
        userChoice = input("Invalid input. Please Enter Your Choice (scissors, paper, or rock)").lower()                      
    print(f"\nYou chose {userChoice}, computer chose {computerChoice}.\n")

    # Using condtional to determine the winner based on the game's rules
    if userChoice == computerChoice:
        print(f"Both players selected {userChoice}. It's a tie!")
    elif userChoice == "rock":
        if computerChoice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif userChoice == "paper":
        if computerChoice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif userChoice == "scissors":
        if computerChoice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    # prompt to ask the user if they want to play again
    play_again = input("Play again? (yes/no): ").lower()

    # Validate the user's input
    while play_again not in ["yes", "no"]:
        play_again = input("Invalid input. Play again? (yes/no): ").lower()
    if play_again == "yes":
        # restart the game
        game()
    else:
        print("Thanks for playing!")

# Start the game
game()
