"""
Case Specific Sorting of Strings

Problem statement:
Given a string consisting of uppercase and lowercase ASCII characters, write a
function, case_sort, that sorts uppercase and lowercase letters separately,
such that if the 𝑖 th place in the original string had an uppercase character
then it should not have a lowercase character after being sorted and vice versa

For example:
Input: fedRTSersUXJ
Output: deeJRSfrsTUX
"""


def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output
            list
        else:
            pick upper-case character from sorted string to place in output
            list

    Note: You can use Python's inbuilt ord() function to find the ASCII value
    of a character
    """

    upper_char_index = 0
    lower_char_index = 0

    sorted_string = sorted(string)

    for index, character in enumerate(sorted_string):
        # Check if character is lowercase
        ascii_int = ord(character)
        # ASCII value of a = 97 & ASCII value of z = 122
        if 97 <= ascii_int <= 122:
            lower_char_index = index
            break

    output = list()
    for character in string:
        ascii_int = ord(character)
        # If character is a lowercase in the given string, then replace with
        # lower case character from sorted string in its position
        if 97 <= ascii_int <= 122:
            output.append(sorted_string[lower_char_index])
            lower_char_index += 1
        else:
            output.append(sorted_string[upper_char_index])
            upper_char_index += 1

    return ''.join(output)


# Tests
test_string_1 = 'fedRTSersUXJ'
print(case_sort(test_string_1))

test_string_2 = "defRTSersUXI"
print(case_sort(test_string_2))