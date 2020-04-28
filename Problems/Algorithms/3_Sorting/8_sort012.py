"""
Problem Statement
Write a function that takes an input array (or Python list) consisting of only
0s, 1s, and 2s, and sorts that array in a single traversal.

Note that if you can get the function to put the 0s and 2s in the correct
positions, this will automatically cause the 1s to be in the correct positions
as well.

Time complexity: O(n)
Space complexity:
    Input space => O(n)
    Auxiliary space (extra or temporary space) => O(1)
    Total space => O(n + 1) => O(n)
"""


def sort_012(input_list):
    """
    The idea is to put 0 and 2 in their correct positions, which will make
    sure all the 1s are automatically placed in their right positions
    """

    low = 0
    high = len(input_list) - 1
    mid = 0

    while (mid <= high):
        if input_list[mid] == 0:
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        elif input_list[mid] == 2:
            input_list[mid], input_list[high] = input_list[high], \
                input_list[mid]
            high -= 1

    return input_list


# Tests
def test_function(testcase):
    sort_012(testcase)
    print(testcase)
    if testcase == sorted(testcase):
        print('Pass')
    else:
        fail


input_list = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(input_list)

test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0,
             2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case)

test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)
