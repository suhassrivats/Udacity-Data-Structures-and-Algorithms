"""
Problem Statement
Suppose there is a staircase that you can climb in either 1 step, 2 steps,
or 3 steps. In how many possible ways can you climb the staircase if the
staircase has n steps? Write a recursive function to solve the problem.

Example:

n = 3
output = 4
The output is 4 because there are four ways we can climb the staircase:

1. 1 step +  1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
4. 3 steps
"""


def staircase(n):
    """
    :param: n - number of steps in the staircase
    Return number of possible ways in which you can climb the staircase
    TODO - write a recursive function to solve this problem
    """
    if n <= 0:
        return 1

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)


# Tests
def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = staircase(n)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


n = 3
solution = 4
test_case = [n, solution]
test_function(test_case)

n = 4
solution = 7
test_case = [n, solution]
test_function(test_case)

n = 7
solution = 44
test_case = [n, solution]
test_function(test_case)
