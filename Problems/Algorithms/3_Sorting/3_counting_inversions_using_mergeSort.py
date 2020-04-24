"""
Counting Inversions
The number of inversions in a disordered list is the number of pairs of
elements that are inverted (out of order) in the list.

Here are some examples:
[0,1] has 0 inversions
[2,1] has 1 inversion (2,1)
[3, 1, 2, 4] has 2 inversions (3, 2), (3, 1)
[7, 5, 3, 1] has 6 inversions (7, 5), (3, 1), (5, 1), (7, 1), (5, 3), (7, 3)
The number of inversions can also be thought of in the following manner.

Given an array arr[0 ... n-1] of n distinct positive integers, for indices i
and j, if i < j and arr[i] > arr[j] then the pair (i, j) is called an
inversion of arr.

Problem statement:
Write a function, count_inversions, that takes an array (or Python list) as
input, and returns a count of the total number of inversions present in the
input.

Mergesort provides an efficient way to solve this problem.
"""


def count_inversions_iterative(arr):
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """

    inversions = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
        i += 1
    return inversions


def count_inversions(arr):
    # Create a temp array to store sorted array in merge function
    n = len(arr)
    temp_arr = [0] * n

    start_index = 0
    end_index = len(arr) - 1
    return _mergeSort(arr, temp_arr, start_index, end_index)


def _mergeSort(arr, temp_arr, start_index, end_index):

    # Inversions counter
    inv_count = 0

    # Make a recursive call only if there are more than one elements
    if start_index < end_index:

        # Mid is calculated to divide the array into two subarrays
        mid = (start_index + end_index) // 2

        # It will calculate the inversion counts in the left subarray
        inv_count += _mergeSort(arr, temp_arr, start_index, mid)

        # It will calculate the inversion counts in the right subarray
        inv_count += _mergeSort(arr, temp_arr, mid+1, end_index)

        # It will merge two subarrays in a sorted subarray
        inv_count += merge(arr, temp_arr, start_index, mid, end_index)

    return inv_count


def merge(arr, temp_arr, start_index, mid, end_index):
    start_index_left = start_index  # Starting index of left subarray
    start_index_right = mid + 1  # Starting index of right subarray
    start_temp_arr = start_index  # Starting index of to be sorted subarray
    inv_count = 0

    # Make sure that start_index_left and start_index_right do not exceed
    # their subarray limits
    while start_index_left <= mid and start_index_right <= end_index:
        # There will be no inversions if
        # arr[start_index_left] <= arr[start_index_right]
        if arr[start_index_left] <= arr[start_index_right]:
            temp_arr[start_temp_arr] = arr[start_index_left]
            start_temp_arr += 1
            start_index_left += 1
        else:
            # Inversion will occur
            temp_arr[start_temp_arr] = arr[start_index_right]
            inv_count += ((mid - start_index_left) + 1)
            start_temp_arr += 1
            start_index_right += 1

    # Copy remaining elements of left subarray to temp_arr
    while start_index_left <= mid:
        temp_arr[start_temp_arr] = arr[start_index_left]
        start_temp_arr += 1
        start_index_left += 1

    # Copy remaining elements of right subarray to temp_arr
    while start_index_right <= end_index:
        temp_arr[start_temp_arr] = arr[start_index_right]
        start_temp_arr += 1
        start_index_right += 1

    # Copy the sorted subarray into original array
    for i in range(start_index, end_index+1):
        arr[i] = temp_arr[i]

    return inv_count


# Tests
arr = [3, 1, 2, 4]
print(count_inversions_iterative(arr))

arr = [1, 20, 6, 4, 5]
result = count_inversions(arr)
print(result)


arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
result2 = count_inversions(arr)
print(result2)