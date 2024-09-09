# Define the number to be guessed by the user
gameNum = 70

# Get the user's initial guess
userNum = int(input("Guess the number: "))

#Prompt the user for input until they guess the correct number
while gameNum != userNum :
    userNum= int(input("You entered wrong number. Guess Again! : "))

print("Congratulation! you entered correct number", gameNum)
