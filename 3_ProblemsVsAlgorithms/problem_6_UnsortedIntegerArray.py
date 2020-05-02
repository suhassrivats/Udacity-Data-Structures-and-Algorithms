import random
"""
Max and Min in a Unsorted Array:
In this problem, we will look for smallest and largest integer from a list of
unsorted integers. The code should run in O(n) time. Do not use Python's
inbuilt functions to find min and max.
"""


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers

    **Complexity Analysis:**
        *Time complexity*  => `O(n)` // iterate through each item in an array
        *Space complexity:*
        - Input space => `O(n)`
        - Auxiliary space => `O(1)`
        - Total space => `O(n + 1)`  => `O(n)`
    """

    if len(ints) == 0:
        return (None, None)

    minval = ints[0]
    maxval = ints[0]

    for num in ints:
        # If minval is greater than current element, then update minval
        if minval > num:
            minval = num

        # If maxval is less than current element, then update maxval
        if maxval < num:
            maxval = num

    return (minval, maxval)


# Example Test Case of Ten Integers
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((2, 2) == get_min_max([2])) else "Fail")
print("Pass" if ((-1, 1) == get_min_max([1, -1])) else "Fail")
print("Pass" if ((None, None) == get_min_max([])) else "Fail")
