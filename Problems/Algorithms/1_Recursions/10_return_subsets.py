"""
Problem Statement
Given an integer array, find and return all the subsets of the array. The
order of subsets in the output array is not important. However the order of
elements in a particular subset should remain the same as in the input array.

Note: An empty set will be represented by an empty list

Example 1

arr = [9]
output = [[]
          [9]]

Example 2

arr = [9, 12, 15]
output =  [[],
           [15],
           [12],
           [12, 15],
           [9],
           [9, 15],
           [9, 12],
           [9, 12, 15]]
"""


def subsets(arr):
    """
    :param: arr - input integer array
    Return - list of lists (two dimensional array) where each list represents a subset
    TODO: complete this method to return subsets of an array
    """
    res = []
    dfs(arr, 0, [], res)
    return res


def dfs(arr, index, path, res):
    res.append(path)
    for i in range(index, len(arr)):
        dfs(arr, i+1, path + [arr[i]], res)

print(subsets([5, 7]))
