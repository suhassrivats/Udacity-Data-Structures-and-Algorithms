"""
Dutch National Flag Problem:
Given an input array consisting on only 0, 1, and 2, sort the array in a
single traversal. You're not allowed to use any sorting function that Python
provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you
traverse the array twice, that would still be an O(n) solution but it will not
count as single traversal.

Reference:
https://www.youtube.com/watch?v=BOt1DAvR0zI
"""


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a
    single traversal.

    Args:
       input_list(list): List to be sorted

    Complexity:
    Time complexity: O(n)
    Space complexity:
        Input space => O(n)
        Auxiliary space => O(1)
        Total space => O(n + 1) => O(n)
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
            input_list[high], input_list[mid] = input_list[mid], \
                input_list[high]
            high -= 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Tests
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
