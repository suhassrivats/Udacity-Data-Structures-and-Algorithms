"""
Problem Statement
Given list of integers that contain numbers in random order, write a program
to find the longest possible sub sequence of consecutive numbers in the array.
Return this subsequence in sorted order. The solution must take O(n) time

For e.g. given the list 5, 4, 7, 10, 1, 3, 55, 2, the output should be
1, 2, 3, 4, 5

Note- If two arrays are of equal length return the array whose index of
smallest element comes first.

Solution logic:
1. Take every element, try to find elements before and after to get a
consecutive seq.
2. Keep repeating this for every element, as long as the given element has not
already been counted as part of another sequence.

Time complexity: O(n)
It is O(n) because every element of the list of processed exactly once, by
keeping track of the elements using the dict. Even though the loops look
nested, it's is not n^2, because the while loop conditions are such that it
will get into the loop only if an element has never been processed earlier.
"""


def longest_consecutive_subsequence(input_list):
    # TODO: Write longest consecutive subsequence solution
    element_dict = dict()

    # iterate over the list and store element in a suitable data structure
    for index, element in enumerate(input_list):
        element_dict[element] = index

    max_length = -1
    starts_at = len(input_list)

    # traverse / go over the data structure in a reasonable order to determine
    # the solution
    for index, element in enumerate(input_list):
        current_starts = index
        element_dict[element] = -1  # Mark the element as visited

        # Counter for consecutive numbers
        current_count = 1

        # check upwards
        current = element + 1
        # if next consecutive number exists in the dictionary and if the
        # element is not visited
        while current in element_dict and element_dict[current] != -1:
            element_dict[element] = -1  # Mark the element as visited
            current_count += 1  # Update the counter by 1
            current += 1  # Increment current by 1 and see if next ele is there

        # check downwards
        current = element - 1
        while current in element_dict and element_dict[current] != -1:
            # Keep track of a new sequence beginning
            current_starts = element_dict[current]

            element_dict[element] = -1  # Mark the element as visited
            current_count += 1  # Update the counter by 1
            current -= 1  # Decrement counter by 1 and check for prev element

        if current_count >= max_length:
            if current_count == max_length and current_starts > starts_at:
                continue
            starts_at = current_starts
            max_length = current_count

    start_element = input_list[starts_at]
    return [element for element in
            range(start_element, start_element + max_length)]


# Tests
def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
test_function(test_case_1)

test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20,
                25, 11, 1, 8, 6], [8, 9, 10, 11, 12]]
test_function(test_case_2)

test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
test_function(test_case_3)

input_list = [1, 2, 3, 4]
print(longest_consecutive_subsequence(input_list))
