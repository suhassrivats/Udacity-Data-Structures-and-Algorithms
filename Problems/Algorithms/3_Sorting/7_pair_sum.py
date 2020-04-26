"""
Problem Statement
Given an input array and a target value (integer), find two values in the
array whose sum is equal to the target value. Solve the problem without using
extra space. You can assume the array has unique values and will never have
more than one solution.
"""


def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    TODO: complete this method to find two numbers such that their sum is
    equal to the target
    Return the two numbers in the form of a sorted list
    """

    front_index = 0
    back_index = len(arr) - 1

    while front_index < back_index:
        # Get the values of front and back based on their index respectively
        front = arr[front_index]
        back = arr[back_index]

        if front + back == target:
            return [front, back]
        elif front + back < target:
            front_index += 1
        else:
            back_index -= 1

    return [None, None]


# Tests
def test_function(testcase):
    input_list = testcase[0]
    target = testcase[1]
    solution = testcase[2]
    output = pair_sum(input_list, target)
    if output == solution:
        print('Pass')
    else:
        print('Fail')


arr = [1, 2, 3, 4, 5, 6]
target = 8
solution = [2, 6]
testcase = [arr, target, solution]
test_function(testcase)

input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [0, 8, 5, 7, 9]
target = 9
solution = [0, 9]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [110, 9, 89]
target = 9
solution = [None, None]
test_case = [input_list, target, solution]
test_function(test_case)
