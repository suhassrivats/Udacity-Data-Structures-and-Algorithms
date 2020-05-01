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
    """
   pass


# Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
