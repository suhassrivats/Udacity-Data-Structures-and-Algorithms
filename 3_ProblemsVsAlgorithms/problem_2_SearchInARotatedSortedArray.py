"""
Search in a Rotated Sorted Array:
You are given a sorted array which is rotated at some random pivot point.
Example:
[0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
You are given a target value to search. If found in the array return its index,
otherwise return -1.
You can assume there are no duplicates in the array and your algorithm's
runtime complexity must be in the order of O(log n).
Example:
Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Approach:
Find a pivot element (using binary search) such that there are two sorted
arrays. Check in which array does the target element reside. Then apply binary
search on that array to find its position.

Reference:
https://www.youtube.com/watch?v=5BI0Rdm9Yhk
"""


def rotated_array_search(input_list, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), target(int): Input array to search and the target
    Returns:
       int: Index or -1

    Complexity:
    Time complexity:
        Finding pivot => O(logn)
        Binary Search => O(logn)
        Total => O(logn)
    Space complexity:
        Input space: O(n) //for input_list
        Auxiliary space: O(1)
        Total space: O(n + 1) => O(n)
    """

    # Check if input_list empty or if there is only one element
    if len(input_list) == 0:
        return -1
    if len(input_list) == 1:
        if input_list[0] == target:
            return 0
        else:
            return -1

    start = 0
    end = len(input_list) - 1
    result = 0

    # If array is fully sorted
    if input_list[start] < input_list[end]:
        # Just do a simple binary search
        result = binary_search(start, end, input_list, target)
    else:
        # Find the pivot element
        pivot_index = find_pivot(start, end, input_list)

        # Check in which sorted array does the target may lie.
        # Check in the right sorted array
        if target >= input_list[pivot_index] and target <= input_list[end]:
            result = binary_search(pivot_index, end, input_list, target)
        else:
            # Check in the left sorted array
            result = binary_search(start, pivot_index-1, input_list, target)

    return result


def find_pivot(start, end, input_list):
    mid = start + (end - start) // 2
    pivot_index = 0

    # Base case
    # If array were sorted, mid+1 would be greater than mid. If not, we found
    # our pivot_index
    if input_list[mid] > input_list[mid + 1]:
        return mid + 1
    else:
        if input_list[start] > input_list[mid]:
            # It means that pivot is in left of mid
            pivot_index = find_pivot(start, mid-1, input_list)
        else:
            # It means that pivot is in the right of mid
            pivot_index = find_pivot(mid+1, end, input_list)

    return pivot_index


def binary_search(start, end, input_list, target):
    while start <= end:
        mid = (start + end) // 2
        if input_list[mid] == target:
            return mid
        else:
            if input_list[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


# Tests
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list,
                                                                 number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], -1])