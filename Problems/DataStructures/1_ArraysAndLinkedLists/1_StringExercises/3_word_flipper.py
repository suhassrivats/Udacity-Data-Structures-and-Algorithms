"""
Reverse the words in sentence:
Given a sentence, reverse each word in the sentence while keeping the order
the same!

"""


def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped

    Assume,
        n - length of string
        s- length of the word

    Time complexity:
        for-loop: O(n)
            word-reverse: O(s)
        join: O(n)
        Total: O(n*s + n) => O(n)

    Space complexity:
        our_string: O(n)
        rev_words: O(n)
        Total: O(n + n) => O(n)
    """

    # TODO: Write your solution here
    rev_words = []

    for word in our_string.split():
        rev_words.append(word[::-1])

    return (' '.join(rev_words))


# Test Cases
print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print("Pass" if ('sihT si na elpmaxe' ==
                 word_flipper('This is an example')) else "Fail")
print("Pass" if ('sihT si eno llams pets rof ...' ==
                 word_flipper('This is one small step for ...')) else "Fail")
