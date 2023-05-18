"""Generate words with lists of letters


Submitted by Jasmine Fan, NetID:jf4654
Using recursive tools to generate words with lists of letters
"""


dictFile = open('Dictionary.txt', 'r')
header = dictFile.readline()
dictList = [line.strip() for line in dictFile if line != "\n"]

word_count = len(dictList)




# Task 2.1
def combinations_fixed_size(input_letters: list):
    """Takes a list of letters and returns them as a list of scrambled words


    param input_letters: a list that contains all the letters of a word
    return list of scrambled words
    """

    new_combos = []

    # Handle Error
    if not input_letters:
        raise ValueError("No word found...")

    # Base Case
    if len(input_letters) == 1:
        return input_letters

    # Recursive Case
    first_letter, simpler_letter_list = input_letters[0], input_letters[1:]
    simpler_combinations = combinations_fixed_size(simpler_letter_list)

    for combo in simpler_combinations:
        for position in range(len(combo) + 1):
            first_part, second_part = combo[0:position], combo[position:]
            new_combos += [first_part + first_letter + second_part]

    # return new_combos
    return list(set(new_combos))




# Task 2.2
def combinations(input_letters: list):
    """Takes a list of letters and returns them as a list of scrambled words (short and long)


    param input_letters: a list that contains all the letters of a word
    return list of scrambled words, all short and long
    """
    new_combos = []

    # Handle Error
    if not input_letters:
        raise ValueError("No word found...")

    # Base Case
    if len(input_letters) == 1:
        return input_letters

    # Recursive Case
    first_letter, simpler_letter_list = input_letters[0], input_letters[1:]
    simpler_combinations = combinations_fixed_size(simpler_letter_list)

    for combo in simpler_combinations:
        for position in range(len(combo) + 1):
            first_part, second_part = combo[0:position], combo[position:]
            new_combos += [first_part + first_letter + second_part]

            # This probably can be simplified, but when I try to simplify it, it doesn't print the reverse of two
            # EX: first_letter + first part = 'AB'
            #     ^^ if I only do this, then only AB will appear, no 'BA'
            # The nested for loop above handles all other sizes of letters, just not all the 2 letter ones
            new_combos += [first_letter + first_part]
            new_combos += [first_part + first_letter]
            new_combos += [first_letter + second_part]
            new_combos += [second_part + first_letter]

    # return new_combos + simpler_combinations + input_letters
    return list(set(new_combos + simpler_combinations + input_letters))




# Task 2.3
def word_search(letter_list: list):
    """Takes a list of letters, uses a threshold of 3, and checks if they are words through a dictionary

    param letter_list: a list that contains all the letters of a word
    return list of actual words, checked by a dictionary
    """
    # Handle Error
    if not letter_list:
        raise ValueError("No word found...")

    # Base Case
    if len(letter_list) <= 2:
        return letter_list

    # Recursive Case
    all_combos = combinations(letter_list)
    filtered_combos = []
    threshold_combos = [combo.upper() for combo in all_combos if len(combo) >= 3]

    for combo in threshold_combos:
        if combo in dictList:
            filtered_combos += [combo]

    # Tried simplifying below, but it kept running and crashed
        # first_letter, simpler_combo_list = combo[0], [letter for letter in combo[1:]]
        # simple_combo = word_search(simpler_combo_list)
        #
        # for combo2 in simple_combo:
        #     if combo2 in dictList:
        #         filtered_combos += [combo2]

    return list(set(filtered_combos))




if __name__ == '__main__':
    print(f"Dictionary Loaded: {word_count} words.")

    check = True
    while check:
        input_word_str = input("\nEnter the letters available; don't use any separators (for example, odijwe) ")
        input_list = [letter for letter in input_word_str]
        print(combinations(input_list))

        print("----------------------------------------------")

        print("Of those, the following satisfied the 3-letter threshold and were found in the Dictionary.txt as follows:")
        print([word.lower() for word in word_search(input_list)])
        cont_check = input("\nPress ENTER to continue, anything else exits ")
        if cont_check != "":
            check = False

    # print(combinations(["A", "B", "C"]))
    # print(len(combinations_fixed_size(["A", "L", "F"])))
