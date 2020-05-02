"""
Finding the Square Root of an Integer:
Find the square root of the integer without using any Python library. You have
to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.
If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose
floor value is 5.

The expected time complexity is O(log(n))

Reference:
https://www.geeksforgeeks.org/square-root-of-an-integer/
"""


def sqrt_naive(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root

    Approach:
    To find the floor of the Square Root, try with all natural numbers starting
    from 1. Contiue to increment the number by 1 until the product of the
    that number with itself is greater than input number.

    Complexity:
    Time complexity => O(sqrt(n))
    Space complexity:
        Input space => O(1)
        Auxiliary space => O(1)
        Total space => O(1 + 1) => O(2) => O(1)
    """

    # Corner case to handle negative numbers
    if number < 0:
        return None

    # Base cases
    if (number == 0 or number == 1):
        return number

    # Staring from 1, try all numbers until i*i is greater than or equal to x
    i = 1
    result = 1
    while result <= number:
        i += 1
        result = i * i

    return i-1


def sqrt(number):
    """
    In the previous approach, we are trying to find square root of a number by
    by multiplying a natural number by iteself (starting from 1, increment
    by 1). This can be further optimized using Binary Search Algorithm

    Complexity:
    Time complexity: O(logn)
    Space complexity:
        Input space: O(1)
        Auxiliary space (extra or temp): O(1)
        Total space: O(1 + 1) => O(2) => O(1)
    """

    # Corner case to handle negative numbers
    if number < 0:
        return None

    if number == 0 or number == 1:
        return number

    start = 1
    end = number

    while start <= end:

        # Find the mid value
        mid = (start + end) // 2

        # If number is a perfect square
        if (mid * mid) == number:
            return mid

        # Since we need floor, we update answer when mid*mid is smaller
        # than x, and move closer to sqrt(x)
        if (mid * mid) < number:
            start = mid + 1
            ans = mid

        # If mid*mid is greater than x
        else:
            end = mid - 1

    return ans


# Tests
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (None == sqrt(-25)) else "Fail")
print("Pass" if (None == sqrt(-1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
