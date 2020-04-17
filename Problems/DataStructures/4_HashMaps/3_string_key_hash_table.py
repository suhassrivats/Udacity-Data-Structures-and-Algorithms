"""
String Key Hash Table
In this quiz, you'll write your own hash table and hash function that uses
string keys. Your table will store strings in buckets by their first two
letters, according to the formula below:

Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter
You can assume that the string will have at least two letters, and the first
two characters are uppercase letters (ASCII values from 65 to 90). You can use
the Python function ord() to get the ASCII value of a letter, and chr() to get
the letter associated with an ASCII value.

You'll create a HashTable class, methods to store and lookup values, and a
helper function to calculate a hash value given a string. You cannot use a
Python dictionary—only lists! And remember to store lists at each bucket, and
not just the string itself. For example, you can store "UDACITY" at index 8568
as ["UDACITY"].
"""


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """TODO: Input a string that's stored in the table."""
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        """TODO: Return the hash value if the string is already in the table.
        Return -1 otherwise."""
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv
        return -1

    def calculate_hash_value(self, string):
        """TODO: Helper function to calulate a
        hash value from a string."""
        value = ord(string[0])*100 + ord(string[1])
        return value


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
