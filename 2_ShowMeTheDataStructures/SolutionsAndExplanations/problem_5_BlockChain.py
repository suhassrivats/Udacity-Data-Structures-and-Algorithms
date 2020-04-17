import hashlib
import datetime

# Current time in UTC format
utc = datetime.datetime.utcnow()


def calc_hash(data, timestamp):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8') + str(timestamp).encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.prev = None  # previous block
        self.previous_hash = previous_hash
        self.hash = calc_hash(str(data), self.timestamp)

    def __repr__(self):
        return (
            f"Block []: {repr(self.data)}\n"
            f"Hash: {repr(self.hash)}\n"
            f"Previous Hash: {repr(self.previous_hash)}\n"
            f"{repr(self.timestamp)}\n"
        )


class BlockChain:

    def __init__(self):
        self.head = None

    def append(self, data, previous_hash):
        # Append block to the end of the linked list
        if self.head is None:
            self.head = Block(utc, data, 0)
            return
        new_head = Block(utc, data, self.head.hash)
        new_head.prev = self.head
        self.head = new_head

    def size(self):
        """Return the size of this linked list"""
        size = 0

        temp = self.head
        while temp:
            size += 1
            temp = temp.prev
        return size

    def to_list(self):
        """Return a list of blocks (nodes) in this linked list"""
        out = []

        block = self.head
        while block:
            out.append(block)
            block = block.prev
        return out


# Testing code
"""
Test Case 1
"""
print("Test Case 1 Empty BlockChain")
A = BlockChain()
print("size", A.size())
print(A.head)
print()


"""
Test Case 2
"""
print("Test Case 2 One item BlockChain")
B = BlockChain()
B.append("Genesis", 0)
print("size", B.size())
for item in B.to_list():
    print(item)
print()

"""
Test Case 3
"""
print("Test Case 3 Two item BlockChain")
C = BlockChain()
C.append("Genesis", 0)
C.append("Exodus", calc_hash("Genesis", utc))


print("size", C.size())
for item in C.to_list():
    print(item)

print()
"""
Test Case 4
"""
print("Test Case 4 Five item BlockChain")
D = BlockChain()
D.append("Genesis", 0)
D.append("Exodus", calc_hash("Genesis", utc))
D.append("Leviticus", calc_hash("Exodus", utc))
D.append("Numbers", calc_hash("Leviticus", utc))
D.append("Deuteronomy", calc_hash("Numbers", utc))

print("size", D.size())
for item in D.to_list():
    print(item)

'''OUTPUT
Test Case 1 Empty BlockChain
size 0
None

Test Case 2 One item BlockChain
size 1
Block []: 'Genesis'
Hash: 'f581efd247abcdbb724758a4de3f0b6f879befdb630dc6c595ceafdd53b4f482'
Previous Hash: 0
datetime.datetime(2020, 4, 15, 7, 6, 53, 379059)


Test Case 3 Two item BlockChain
size 2
Block []: 'Exodus'
Hash: '8bc1a5e463315e1f1bf7562fa658f13796e0c86dd0e7c1e06fa5bbd034d1dc04'
Previous Hash: 'f581efd247abcdbb724758a4de3f0b6f879befdb630dc6c595ceafdd53b4f482'
datetime.datetime(2020, 4, 15, 7, 6, 53, 379059)

Block []: 'Genesis'
Hash: 'f581efd247abcdbb724758a4de3f0b6f879befdb630dc6c595ceafdd53b4f482'
Previous Hash: 0
datetime.datetime(2020, 4, 15, 7, 6, 53, 379059)


Test Case 4 Five item BlockChain
size 5
Block []: 'Deuteronomy'
Hash: '484f71ab15bea6394c7ccfd3fe63c6a80c34d0ec6bbc7b3afd703cee9a48058b'
Previous Hash: '2c56a0bfa965f05e28f399b84b73605bebdabd905e5e768d0d50e1479198a24f'
datetime.datetime(2020, 4, 15, 7, 6, 53, 379059)

Block []: 'Numbers'
Hash: '2c56a0bfa965f05e28f399b84b73605bebdabd905e5e768d0d50e1479198a24f'
Previous Hash: '43cbfdb273b5cf67b4d831e82352c83338847bfbe7b40fdef7f53fdf906328d4'
datetime.datetime(2020, 4, 15, 7, 6, 53, 379059)

Block []: 'Leviticus'
Hash: '43cbfdb273b5cf67b4d831e82352c83338847bfbe7b40fdef7f53fdf906328d4'
Previous Hash: '8bc1a5e463315e1f1bf7562fa658f13796e0c86dd0e7c1e06fa5bbd034d1dc04'
datetime.datetime(2020, 4, 15, 7, 6, 53, 379059)

Block []: 'Exodus'
Hash: '8bc1a5e463315e1f1bf7562fa658f13796e0c86dd0e7c1e06fa5bbd034d1dc04'
Previous Hash: 'f581efd247abcdbb724758a4de3f0b6f879befdb630dc6c595ceafdd53b4f482'
datetime.datetime(2020, 4, 15, 7, 6, 53, 379059)

Block []: 'Genesis'
Hash: 'f581efd247abcdbb724758a4de3f0b6f879befdb630dc6c595ceafdd53b4f482'
Previous Hash: 0
datetime.datetime(2020, 4, 15, 7, 6, 53, 379059)

'''
