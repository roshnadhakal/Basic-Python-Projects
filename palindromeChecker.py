word = input("Enter a word: ")
reverse_word = word[::-1]

if(reverse_word == word):
    print("The word",word,"is a palindrome")
else:
    print("The word",word,"is not a palindrome")
