gameNum = 70
userNum = int(input("Guess the number: "))
while gameNum != userNum :
    userNum= int(input("You entered wrong number. Guess Again! : "))

print("Congratulation! you entered correct number", gameNum)
