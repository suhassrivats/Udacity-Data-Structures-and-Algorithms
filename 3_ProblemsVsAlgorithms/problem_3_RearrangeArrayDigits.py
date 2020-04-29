"""
Rearrange Array Elements:
Rearrange Array Elements so as to form two number such that their sum is
maximum. Return these two numbers. You can assume that all array elements are
in the range [0, 9]. The number of digits in both the numbers cannot differ by
more than 1. You're not allowed to use any sorting function that Python
provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be
[542, 31]. In scenarios such as these when there are more than one possible
answers, return any one.

Here is some boilerplate code and test cases to start with:
"""


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is
    maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums

    Complexity:
    Time complexity:
        Sorting: O(nlogn)
        2-for loops: O(logn + logn) => O(logn)
        Total: O(nlogn + logn) => O(nlogn)
    Space complexity:
        Input space: O(n)
        Auxiliary space (extra or temporary space): O(n) // for sorted_input
        Total: Input space + Auxiliary space => O(n + n) => O(n)
    """

    x = 0
    y = 0
    sorted_input = sorted(input_list, reverse=True)

    for i in range(0, len(sorted_input), 2):
        x = x * 10 + sorted_input[i]

    for j in range(1, len(sorted_input), 2):
        y = y * 10 + sorted_input[j]

    return [x, y]


# Tests
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
