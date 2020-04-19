"""
Write a function that returns a boolean value indicating whether an element
is present, but with no information about the location of that element.
"""


def recursive_binary_search(target, source, left=0):
    """
    Loose wrapper for recursive binary search, returning True if the index is
    found and False if not
    """
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:],
                                       left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)


def contains_using_BS_wrapper(target, source):
    return recursive_binary_search(target, source) is not None


def contains(target, source):
    if len(source) == 0:
        return None
    center = len(source) // 2
    if source[center] == target:
        return True
    elif source[center] < target:
        return contains(target, source[center+1:])
    else:
        return contains(target, source[:center])


# Tests
letters = ['a', 'c', 'd', 'f', 'g', 'h', 'i']
print(contains('a', letters))  # True
print(contains('i', letters))  # False
