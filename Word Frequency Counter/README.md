# Word Frequency Counter

A simple Python script that counts the frequency of each word in a given text file. This project is built using Python 3.12.4.

## Features

- Reads a text file and counts the occurrences of each word.
- Outputs the frequency of each word in a user-friendly format.
- Handles case insensitivity by converting all words to lowercase.

## How to Use

1. Ensure you have Python 3.12.4 or higher installed on your machine.
2. Create a text file named \`wordfile.txt\` in the same directory as the script. Populate it with the text you want to analyze.
3. Run the script using the following command:

   \`\`\`bash
   python word_freq_counter.py
   \`\`\`

4. The script will read the contents of \`wordfile.txt\` and print the frequency of each word.

## Code Explanation

The main function of the script is \`word_freq_counter(wordfile)\`, which performs the following steps:

- Initializes an empty dictionary to store word frequencies.
- Reads the content of the specified text file.
- Splits the text into individual words.
- Iterates over each word, converting it to lowercase to ensure case insensitivity.
- Updates the word frequency in the dictionary.
- Prints the frequency of each word.

## Example

Given a \`wordfile.txt\` with the following content:

\`\`\`
Hello world
Hello everyone
\`\`\`

The output will be:


The word 'hello' appears '2' times.  
The word 'world' appears '1' times.  
The word 'everyone' appears '1' times.  


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a new issue or submit a pull request.
