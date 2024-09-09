# Take input from the user for a word
word = input("Enter a word: ")

# Reverse the word using string slicing [::-1]
reverse_word = word[::-1]

# If the word is the same forwards and backwards, it is a palindrome
if(reverse_word == word):
    print("The word",word,"is a palindrome")
else:
    print("The word",word,"is not a palindrome")
