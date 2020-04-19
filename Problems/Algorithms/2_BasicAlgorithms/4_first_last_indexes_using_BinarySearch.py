"""
Problem statement
Given a sorted array that may have duplicate values, use binary search to
find the first and last indexes of a given value.

For example, if you have the array [0, 1, 2, 2, 3, 3, 3, 4, 5, 6] and the
given value is 3, the answer will be [4, 6] (because the value 3 occurs first
at index 4 and last at index 6 in the array).

The expected complexity of the problem is 𝑂(𝑙𝑜𝑔(𝑛))
"""


def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """

    first_element = find_first_element(arr, number)
    last_element = find_last_element(arr, number)

    return [first_element, last_element]


def find_first_element(arr, target):
    start = 0
    end = len(arr) - 1
    index = -1

    while start <= end:
        mid = int((start + end) / 2)
        if arr[mid] == target:
            # mid could be possible first occurence. So store it in index
            index = mid
            # move left
            end = mid - 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return index


def find_last_element(arr, target):
    start = 0
    end = len(arr) - 1
    index = -1
    while start <= end:
        mid = int((start + end) / 2)
        if arr[mid] == target:
            index = mid
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return index


# Tests
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)
