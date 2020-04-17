"""
Problem Statement
You have been given an array containg numbers. Find and return the largest
sum in a contiguous subarray within the input array.

Example 1:
arr = [1, 2, 3, -4, 6]
The largest sum is 8, which is the sum of all elements of the array.

Example 2:
arr = [1, 2, -5, -4, 1, 6]
The largest sum is 7, which is the sum of the last two elements of the array.

Useful link:
https://www.youtube.com/watch?v=kekmCQXYwQ0
https://www.youtube.com/watch?v=86CQq3pKSUw
"""


def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr

    Example: arr = [-2, 3, 2, -1]

    i 0  1 2 3
    c -2 3 5 4
    g -2 3 5 5

    max_current is max of current element or (previous max of subarrary +
    current-element). For instance, if we are at position 1 of the array
    (value=3), max current is:
    max(3, (-2+3)) = 3
    max(2, (3+2)) = 5
    max(-1, (5-1)) = 4
    """

    max_current = arr[0]
    max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], (max_current+arr[i]))

        if max_current > max_global:
            max_global = max_current

    return max_global


# Test Cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 3, -4, 6]
solution = 8  # sum of array
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements
test_case = [arr, solution]
test_function(test_case)

arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]
test_case = [arr, solution]
test_function(test_case)
