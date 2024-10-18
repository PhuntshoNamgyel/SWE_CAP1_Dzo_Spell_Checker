# SWE_CAP1_Dzo_Spell_Checker

## Project Overview
* The Dzongkha Spell Checker is a software tool created to help users to identify and correct spelling errors in Dzongkha. This project aims to boost the precision of written Dzongkha by providing a reliable and efficient spell-checking solution, making it easier for users to communicate effectively in Dzongkha.

* The purpose of the Dzongkha Spell Checker is to promote better literacy and communication in Dzongkha by allowing users to readily detect and correct spelling mistakes in their writing. This tool is especially useful for students and educators who work with Dzongkha text on a daily-basis, ensuring that their written content is flawless. 

* Main Features:
1. Word Comparison: The spell checker compares words from the input text against the cleaned dictionary of Dzongkha words.

2. Line and Position Tracking: For each misspelled word, the tool provides detailed feedback, including the line number and position within the line, making it easy for users to locate and correct errors.

3. User-Friendly Output: The results are presented in a clear and organized format, allowing users to quickly review incorrect words and their respective locations in the text.

4. Customizable Dictionary: Users can easily update the dictionary to include new words, ensuring the spell checker remains relevant and effective.



## Table of Contents
1. Usage
2. Implementation Details
3. Data Structures
4. Algorithms
5. Challenges and Solutions
6. Future Improvements
7. References


## 1. Usage
To use the Dzongkha spell checker, you need to run the Python script from the command line with the input file containing the Dzongkha text to be checked. The expected input is a .txt file, and the output will be printed in the terminal, showing any misspelled words, along with their line number and position in the line.

```bash
python SWE_CAP1_02240354.py 354.txt
```

## 2. Implementation Details
The spell checker is implemented in Python. It reads the input text and the cleaned dictionary of valid Dzongkha words. The program processes the text, breaking it down line by line and word by word. Each word is compared against the dictionary. If the word is not found in the dictionary, it is marked as incorrect, and its line number and position are recorded.

The core components of the project include:

* File reading: Efficiently reading the input text and the dictionary file.
* Error reporting: Outputting details such as line number and word position for all misspelled words.

## 3. Data Structures
Several data structures are utilized in the Dzongkha Spell Checker to ensure efficient spell-checking:

* Set: The cleaned dictionary of valid Dzongkha words is stored as a set. This allows for quick lookup operations, as set membership tests have an average time complexity of O(1).
* List: The input text is processed into a list of lists, where each sublist represents the words in a specific line of the text. This structure facilitates line-by-line and word-by-word comparisons.
* Tuple: Incorrect words, along with their line numbers and positions, are stored as tuples to keep track of errors.

## 4. Algorithms
The key algorithms used in the spell checker include:

* File Parsing: Both the input file and the dictionary file are read into memory using Python’s built-in open() function. The input text is split into lines, and each line is further split into individual words.
 * Set Membership Test: Each word from the input text is compared against the dictionary using set membership (word in dictionary). This operation is efficient due to the use of sets.
* Error Detection: For each word not found in the dictionary, the algorithm records its line number and position. These details are stored and printed for the user to correct.

## 5. Performance Analysis
The spell checker performs efficiently due to its use of a set for dictionary lookups. The time complexity for checking each word in the input text is O(1), and the total complexity is O(n), where n is the number of words in the input file. The memory usage is moderate, with the main memory overhead coming from loading the dictionary into a set.

* Optimizations:
Using a set for the dictionary lookup speeds up the process significantly compared to using lists, where the time complexity for lookup would be O(n) for each word.
Breaking the text into lines and words upfront reduces the complexity of word processing during the comparison phase.


## 7. Challenges and Solutions
1. Handling Special Characters: Dzongkha script involves unique characters that may not be handled correctly with default text processing tools. This was resolved by ensuring the input files were encoded in UTF-8.
2. Dictionary Size: A comprehensive Dzongkha dictionary is required for accurate spell-checking. Initially, the dictionary was incomplete, leading to false positives. To solve this, the dictionary was manually cleaned and expanded.
3. Performance on Large Files: Processing large input files posed a challenge. By using a set for the dictionary and breaking the input text into manageable chunks (lines), the performance issues were mitigated.


## 8. Future Improvements
1. User Interface: Developing a graphical user interface (GUI) or web-based interface for the spell checker could improve usability.
2. Word Suggestions: Currently, the tool only identifies misspelled words. In the future, adding word suggestions (similar to auto-correct) would make it more helpful.
3. Contextual Checking: Future versions could include context-based spell-checking to identify homophones or grammatical errors that go beyond simple spelling mistakes.
4. Integration: Incorporating this spell checker into popular Dzongkha typing software or text editors could expand its usability.


## 9. References
1. File Operations (https://k4y0x13.github.io/CSF101-Programming-Methodology/unit2/8.file-operations.html)
2. Input and Output - Python (https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
3. Expressions - Python (https://docs.python.org/3/reference/expressions.html#membership-test-operations)
4. Built-in-Types - Python (https://docs.python.org/3/library/stdtypes.html#string-methods)
5. ChatGPT (https://chatgpt.com/)