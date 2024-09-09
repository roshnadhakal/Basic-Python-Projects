
def word_freq_counter(wordfile):
    # Initialize an empty dictionary to store word frequencies
    word_freq = {}

    with open(wordfile, "r") as f:
        text = f.read()

    # split the text into individual words
    words = text.split()

    # iterate over each word in the list of words
    for word in words:
        word = word.lower() #for case insensitivity
        # if the word is already in the dictionary, increment its count
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # print the frequency of each word
    for word, freq in word_freq.items():
        print(f"The word '{word}' appears '{freq}' times.")

word_freq_counter('wordfile.txt')
    





       
