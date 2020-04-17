"""
Problem Statement
The Tower of Hanoi is a puzzle where we have three rods and n disks.
The three rods are:

1. source
2. destination
3. auxiliary
Initally, all the n disks are present on the source rod. The final objective
of the puzzle is to move all disks from the source rod to the destination rod
using the auxiliary rod. However, there are some rules according to which this
has to be done:

1. Only one disk can be moved at a time.
2. A disk can be moved only if it is on the top of a rod.
3. No disk can be placed on the top of a smaller disk.
You will be given the number of disks num_disks as the input parameter.

For example, if you have num_disks = 3, then the disks should be moved as
follows:

    1. move disk from source to auxiliary
    2. move disk from source to destination
    3. move disk from auxiliary to destination
You must print these steps as follows:

    S A
    S D
    A D
Where S = source, D = destination, A = auxiliary
"""


def print_move(frm, to):
    print("%s %s" % (frm, to))


def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks
    TODO: print the steps required to move all disks from source to destination
    """
    tower_of_Hanoi_helper(num_disks, 'S', 'D', 'A')


def tower_of_Hanoi_helper(num_disks, source, destination, auxiliary):

    if num_disks == 0:
        return

    if num_disks == 1:
        print_move(source, destination)
        return

    # Copy n-1 disks from source to spare (auxiallary) rod
    tower_of_Hanoi_helper(num_disks-1, source, auxiliary, destination)

    # Copy remaining 1 disk from source to destination
    tower_of_Hanoi_helper(1, source, destination, auxiliary)

    # Copy n-1 in spare to destination
    tower_of_Hanoi_helper(num_disks-1, auxiliary, destination, source)


# Tests
tower_of_Hanoi(2)
print('*' * 10)
tower_of_Hanoi(3)
print('*' * 10)
tower_of_Hanoi(4)
