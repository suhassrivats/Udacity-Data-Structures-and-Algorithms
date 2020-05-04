"""
Min Operations
Starting from the number 0, find the minimum number of operations required to
reach a given positive target number. You can only use the following two
operations:

1. Add 1
2. Double the number

Example:
For Target = 18, output = 6, because it takes at least 6 steps shown below to
reach the target

start = 0
step 1 ==> 0 + 1 = 1
step 2 ==> 1 * 2 = 2 # or 1 + 1 = 2
step 3 ==> 2 * 2 = 4
step 4 ==> 4 * 2 = 8
step 5 ==> 8 + 1 = 9
step 6 ==> 9 * 2 = 18
For Target = 69, output = 9, because it takes at least 8 steps to reach 69
from 0 using the allowed operations

start = 0
step 1 ==> 0 + 1 = 1
step 2 ==> 1 + 1 = 2
step 3 ==> 2 * 2 = 4
step 4 ==> 4 * 2 = 8
step 5 ==> 8 * 2 = 16
step 6 ==> 16 + 1 = 17
step 7 ==> 17 * 2 = 34
step 8 ==> 34 * 2 = 68
step 9 ==> 68 + 1  = 69
"""


def min_operations(target):
    """
    Return number of steps taken to reach a target number
    input:- target number an integer
    output:- number of steps an integer
    """
    num_steps = 0

    # start backwards from the target
    # if target is odd --> subtract 1
    # if target is even --> divide by 2
    while target != 0:
        if target % 2 == 0:
            target = target // 2

        else:
            target = target - 1

        num_steps += 1

    return num_steps


# Tests
def test_function(testcase):
    target = testcase[0]
    solution = testcase[1]
    output = min_operations(target)

    if output == solution:
        print('Pass')
    else:
        print('Fail')


target = 18
solution = 6
test_case = [target, solution]
test_function(test_case)

target = 69
solution = 9
test_case = [target, solution]
test_function(test_case)

target = 64
solution = 7
test_case = [target, solution]
test_function(test_case)
