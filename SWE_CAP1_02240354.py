################################
"https://github.com/PhuntshoNamgyel/SWE_CAP1_Dzo_Spell_Checker.git"
# 

# Phuntsho Namgyel
# 'A'
# 02240354
################################
# REFERENCES
# https://k4y0x13.github.io/CSF101-Programming-Methodology/unit2/8.file-operations.html
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/3/reference/expressions.html#membership-test-operations
# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://chatgpt.com/

# PROBLEM STATEMENT
# You are tasked with creating a spell checker for the Dzongkha language. Your program should read a Dzongkha text file (dzo.txt) that contains multiple spelling errors which will be provided by the tutor (refer Accessing Input File section). The program should identify and report these errors.


# SOLUTION
###############################

## Removing all noise and cleaning the txt file and deleting unnecessary texts

import re

def clean_dzongkha_line(line):
    # Retain only Dzongkha Unicode characters (U+0F00 to U+0FFF).
    cleaned = re.sub(r'[^\u0F00-\u0FFF།]', '', line)  # Keep only Dzongkha characters and "།"
    cleaned = cleaned.strip()  # Remove leading/trailing spaces
    return cleaned

def process_dzongkha_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            cleaned_line = clean_dzongkha_line(line)
            if cleaned_line:  # Only process non-empty lines
                # Split the cleaned line by "།" and write each part to a new line
                for part in cleaned_line.split('།'):
                    part = part.strip()  # Remove any extra spaces
                    if part:  # Only write non-empty parts
                        outfile.write(part + '།\n')  # Append "།" back and write

input_file = 'dictionary.txt'  # Dictionary txt file
output_file = 'cleaned_dictionary.txt'  # Cleaned txt file

process_dzongkha_file(input_file, output_file)



## Downloading input.txt using URL provided by Sir

import requests # Import the requests library to handle HTTP requests

# URL of the file to be downloaded
url = ('https://csf101-server-cap1.onrender.com/get/input/354')

# Send a GET request to the specified URL
r = requests.get(url)

# Open file named '354.txt' in write-binary mode ('wb')
with open('354.txt', 'wb') as file:
    # Write the content of the response to the file
    data = file.write(r.content)


## Read input.txt file

def read_input_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

input_lines = read_input_file('354.txt')


## Read cleaned_dictionary.txt file

def read_cleaned_dictionary(filename):
    # Open the cleaned dictionary file in read mode with UTF-8 encoding
    # This ensures that we correctly read any special characters in the Dzongkha language
    with open(filename, 'r', encoding='utf-8') as file:
        # Read the entire content of the file and split it into lines
        # Using splitlines() returns a list where each element corresponds to a line in the file
        # We convert this list into a set to store unique words for faster lookup
        return set(file.read().splitlines())

# Call the function to read the cleaned dictionary from 'cleaned_dictionary.txt'
# The result will be a set of words that we can use for spell-checking
cleaned_dictionary = read_cleaned_dictionary('cleaned_dictionary.txt')


## Process the Dzongkha text from 354.txt

def process_dzongkha_text(input_lines):
    # Split each line into a list of words
    # This will create a list of lists, where each inner list contains the words from a line
    return [line.split() for line in input_lines]

# Use the input_lines from 354.txt
processed_text = process_dzongkha_text(input_lines)


## Comparing words of 354.txt with cleaned_dictionary.txt

def compare_with_dictionary(processed_text, dictionary):
    # Create a list to store tuples of incorrect words along with their line number and position
    incorrect_words = []
    
    # Iterate over each line in the processed text
    # 'enumerate' provides the line number starting from 1
    for line_number, words in enumerate(processed_text, start=1):
        # Iterate over each word in the current line
        # 'enumerate' also provides the position of the word starting from 1
        for position, word in enumerate(words, start=1):
            # Check if the word is not present in the cleaned dictionary
            if word not in dictionary:
                # If the word is incorrect, append a tuple to the list with:
                # - line number
                # - position of the word in that line
                # - the incorrect word itself
                incorrect_words.append((line_number, position, word))
    
    # Return the list of incorrect words found
    return incorrect_words

# Call the function to compare the processed text against the cleaned dictionary
incorrect_words = compare_with_dictionary(processed_text, cleaned_dictionary)


## Printing Incorrect Words

def print_incorrect_words(incorrect_words):
    # Check if there are any incorrect words found
    # If the list is empty, print a message and exit the function
    if not incorrect_words:
        print("No incorrect words found.")
        return
    
    # Print the header for the output table
    print("Incorrect words found:")
    print("Line Number | Position | Word")
    print("-----------------------------")
    
    # Iterate through the list of incorrect words
    # Each element is a tuple containing (line_number, position, word)
    for line_number, position, word in incorrect_words:
        # Print each incorrect word's line number, position, and the word itself
        # Using formatted strings to align output neatly
        print(f"{line_number:<11} | {position:<8} | {word}")

# Call the function to print the incorrect words found
print_incorrect_words(incorrect_words)

