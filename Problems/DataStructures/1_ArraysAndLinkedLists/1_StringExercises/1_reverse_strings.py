"""
Reverse Strings:
In this first exercise, the goal is to write a function that takes a string as
input and then returns the reversed string. For example, if the input is the
string "water", then the output should be "retaw".

While you're working on the function and trying to figure out how to
manipulate the string, it may help to use the print statement so you can
see the effects of whatever you're trying.

"""


def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string

    Time complexity:
        for-loop: O(n)
        Total: O(n)
    Space complexity:
        our_string: O(n)
        rev_string: O(n)
        Total: O(n+n) => O(n)
    """

    # TODO: Write your solution here
    rev_string = ''

    # O(n)
    for i in range(len(our_string)):
        rev_string += our_string[(len(our_string)-1) - i]

    return rev_string


def string_reverser_pythonicway(our_string):
    """
    Time complexity:
        string reverse: O(n)
        Total: O(n)
    Space complexity:
        rev_string: O(n)
        Total: O(n)
    """
    return our_string[::-1]


# Test Cases
print('Reverse a string - The old fashonied way:')
print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print("Pass" if ('!noitalupinam gnirts gnicitcarP' ==
                 string_reverser('Practicing string manipulation!'))
      else "Fail")
print("Pass" if ('3432 :si edoc esuoh ehT' ==
                 string_reverser('The house code is: 2343')) else "Fail")

print('Reverse a string - The Python Way:')
print("Pass" if ('retaw' == string_reverser_pythonicway('water')) else "Fail")
print("Pass" if ('!noitalupinam gnirts gnicitcarP' ==
                 string_reverser_pythonicway('Practicing '
                                             'string manipulation!'))
      else "Fail")
print("Pass" if ('3432 :si edoc esuoh ehT' ==
                 string_reverser_pythonicway('The house code '
                                             'is: 2343')) else "Fail")
