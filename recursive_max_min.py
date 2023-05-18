"""Finding the min and max of a list


Submitted by Jasmine 
Using recursion to find the min and max values of a list
"""


# Find MAX value
def find_max_value(input_list: list):
    if not input_list:
        raise ValueError("List is empty...")

    # Base Case
    if len(input_list) == 1:
        return input_list[0]

    # Recursive case
    sub_list1, sub_list2 = input_list[:len(input_list)//2], input_list[(len(input_list) // 2) + 1:]

    sub1_max = find_max_value(sub_list1)
    sub2_max = find_max_value(sub_list2)

    return sub1_max if sub1_max > sub2_max else sub2_max


# Find MIN value
def find_min_value(input_list: list):
    if not input_list:
        raise ValueError("List is empty...")

    # Base Case
    if len(input_list) == 1:
        return input_list[0]

    # Recursive case
    sub_list1, sub_list2 = input_list[:len(input_list)//2], input_list[(len(input_list) // 2) + 1:]

    sub1_min = find_min_value(sub_list1)
    sub2_min = find_min_value(sub_list2)

    return sub1_min if sub1_min < sub2_min else sub2_min
