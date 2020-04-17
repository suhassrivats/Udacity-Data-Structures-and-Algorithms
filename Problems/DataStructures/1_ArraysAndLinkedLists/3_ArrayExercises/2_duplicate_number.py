"""
You have been given an array of length = n. The array contains integers
from 0 to n - 2. Each number in the array is present exactly once except for
one number which is present twice. Find and return this duplicate number
present in the array

Example:

arr = [0, 2, 3, 1, 4, 5, 3]
output = 3 (because 3 is present twice)
The expected time complexity for this problem is O(n) and the expected
space-complexity is O(1).

Note:

There are multiple ways of solving this problem. I could think of below 3
1) Comparing element by element - O(n^2)
2) Sort and then compare - nlog(n)
3) Put it in dictionary and find an element with more than 1 count - O(n) but
space will be O(n) as well.
"""


def duplicate_number(arr):
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    current_sum = 0
    expected_sum = 0

    for num in arr:
        current_sum += num

    for i in range(len(arr)-1):
        expected_sum += i

    return current_sum - expected_sum


# Test cases
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [0, 0]
solution = 0
test_case = [arr, solution]
test_function(test_case)

arr = [0, 2, 3, 1, 4, 5, 3]
solution = 3
test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 4, 3, 2, 0]
solution = 0
test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 5, 5, 3, 2, 4]
solution = 5
test_case = [arr, solution]
test_function(test_case)
