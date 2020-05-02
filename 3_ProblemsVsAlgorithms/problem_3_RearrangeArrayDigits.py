"""
Rearrange Array Elements:
Rearrange Array Elements so as to form two number such that their sum is
maximum. Return these two numbers. You can assume that all array elements are
in the range [0, 9]. The number of digits in both the numbers cannot differ by
more than 1. You're not allowed to use any sorting function that Python
provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be
[542, 31]. In scenarios such as these when there are more than one possible
answers, return any one.

Approach:
Given an array of integers between 0 to 9, find two numbers with maximum sum
formed by using all digits of the array. We know that a maximum number can be
formed from given digits (0-9) when the largest digit appears first, second
largest digit appears second, and so on.. finally the smallest digit appears
in the end.

Reference:
https://www.techiedelight.com/find-two-numbers-maximum-sum-array-digits/
"""


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is
    maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums

    Complexity:
    Time complexity:
        Sorting: O(nlogn)
        2-for loops: O(logn + logn) => O(logn)
        Total: O(nlogn + logn) => O(nlogn)
    Space complexity:
        Input space: O(n)
        Auxiliary space (extra or temporary space): O(n) // for sorted_input
        Total: Input space + Auxiliary space => O(n + n) => O(n)
    """

    x = 0
    y = 0

    # Sorted input in reverse order
    sorted_input = mergesort(input_list)[::-1]

    for i in range(0, len(sorted_input), 2):
        x = x * 10 + sorted_input[i]

    for j in range(1, len(sorted_input), 2):
        y = y * 10 + sorted_input[j]

    return [x, y]


def mergesort(items):

    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    # Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)

    # Merge our two halves and return
    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        # If left's item is larger, append right's item
        # and increment the index
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        # Otherwise, append left's item and increment
        else:
            merged.append(left[left_index])
            left_index += 1

    # Append any leftovers. Because we've broken from our while loop,
    # we know at least one is empty, and the remaining:
    # a) are already sorted
    # b) all sort past our last element in merged
    merged += left[left_index:]
    merged += right[right_index:]

    # return the ordered, merged list
    return merged


# Tests
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[],[]])
test_function([[1],[1]])