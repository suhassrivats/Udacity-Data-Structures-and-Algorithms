"""
Permutation
Let's use recursion to help us solve this permutation problem:

Given a list of items, the goal is to find all of the permutations of that
list. For example, if given a list like: ["apple", "water"], you could create
two permuations from it. One in the form of the original input and one in the
reversed order like so: ["water","apple"]
"""

import copy


def permute(lst):
    """
    Return a list of permutations

    Examples:
       permute([0, 1]) returns [ [0, 1], [1, 0] ]

    Args:
      l(list): list of items to be permuted

    Returns:
      list of permutation with each permuted item be represented by a list
    """
    if len(lst) == 0:
        return [[]]
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            m = lst[i]
            remLst = lst[:i] + lst[i+1:]
            for p in permute(remLst):
                l.append([m] + p)
        return l


# Test Cases
# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.

    Note that the ordering of the list is not important.

    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list

    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input

    o.sort()
    e.sort()
    return o == e


print("Pass" if (check_output(permute([]), [[]])) else "Fail")
print("Pass" if (check_output(permute([0]), [[0]])) else "Fail")
print("Pass" if (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print("Pass" if (check_output(permute([0, 1, 2]), [[0, 1, 2], [
      0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")
