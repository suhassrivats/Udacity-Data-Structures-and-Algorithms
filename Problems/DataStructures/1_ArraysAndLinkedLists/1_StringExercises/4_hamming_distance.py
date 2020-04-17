"""
Hamming Distance:
In information theory, the Hamming distance between two strings of equal
length is the number of positions at which the corresponding symbols are
different.

Calculate the Hamming distace for the following test cases.

"""


def hamming_distance(str1, str2):
    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming
       distance
    Returns:
       int: Hamming Distance

    Time complexity:
        for-loop: O(n)
        others: O(1)
        Total: O(n)

    Space complexity:
        str1, str2: O(n + m) => O(2n) => O(n) //since n=m in this case
        count: O(1)
        Total: O(n + 1) => O(n)
    """

    # TODO: Write your solution here
    if len(str1) == len(str2):  # O(1)
        count = 0  # O(1)

        for i in range(len(str1)):  # O(n)
            if str1[i] != str2[i]:  # O(1)
                count += 1  # O(1)

        return count

    else:
        return None


# Test cases
print("Pass" if (10 == hamming_distance('ACTTGACCGGG', 'GATCCGGTACA'))
      else "Fail")
print("Pass" if (1 == hamming_distance('shove', 'stove')) else "Fail")
print("Pass" if (None == hamming_distance(
    'Slot machines', 'Cash lost in me')) else "Fail")
print("Pass" if (9 == hamming_distance('A gentleman', 'Elegant men'))
      else "Fail")
print("Pass" if (2 == hamming_distance(
    '0101010100011101', '0101010100010001')) else "Fail")
