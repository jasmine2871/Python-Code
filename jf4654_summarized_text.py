"""Prints first letter, amount of characters inbetween, and last letter for words of a sentence.


Submitted by Jasmine Fan, NetID: jf4654
This script uses multiple assignments to summarize a word and joins it to create a summarized sentence.
"""
while True:
    # Task 2.1. Separate the text into words and identify the beginning and end of each word
    inputString = input("Provide an input string: ")
    if inputString == "":
        exit()
    print()
    inputList = inputString.split(" ")

    newSentence = ""
    trimWordList = []
    first_letter = ""
    middle_part = ""
    last_letter = ""
    for word in inputList:
        storedWord = ""
        newWord = ""

        # Task 2.2. Make the summarized version of each word and concatenate it with its punctuation
        for char in word:
            if char.isalpha() or (char in ['-', '_']):
                storedWord += storedWord.join(char)

        try:
            first_letter, *middle_part, last_letter = storedWord
        except ValueError:
            trimWordList += [word]
        else:
            if len(middle_part) == 0:
                trimWord = word
            else:
                newWord = first_letter + str(len(middle_part)) + last_letter
                trimWord = word.replace(storedWord, newWord)
            trimWordList += [trimWord]

    print('Your summarized sentence is: ')
    newSentence = " ".join(trimWordList)
    print(newSentence)
    print()

# Test lines:
# This is pre-made lemonade. However, it tastes like it was 'homemade' a week ago.
# This is a simple, but useful example! However, there are many cases not included here...
