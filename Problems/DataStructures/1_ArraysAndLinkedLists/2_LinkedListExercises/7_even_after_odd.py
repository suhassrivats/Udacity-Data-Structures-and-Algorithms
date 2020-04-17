"""
Problem Statement
Given a linked list with integer data, arrange the elements in such a manner
that all nodes with even numbers are placed after odd numbers. Do not create
any new nodes and avoid using any other data structure. The relative order
of even and odd elements must not change.

Example:
linked list = 1 2 3 4 5 6
output = 1 3 5 2 4 6

Useful link:
https://www.youtube.com/watch?v=gmfi2NMJJmc
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """

    if head is None:
        return None

    evenHead = None
    oddHead = None
    lastEven = None
    lastOdd = None
    current_node = head

    while current_node is not None:

        # If current node is even
        if current_node.data % 2 == 0:
            if evenHead is None:
                evenHead = current_node
                lastEven = current_node
            else:
                lastEven.next = current_node
                lastEven = current_node

        # If current node is odd
        else:
            if oddHead is None:
                oddHead = current_node
                lastOdd = current_node
            else:
                lastOdd.next = current_node
                lastOdd = current_node

        current_node = current_node.next

        # Merge odd and even. Odd will go first
        if oddHead is not None:
            head = oddHead

        if lastOdd is not None:
            lastOdd.next = evenHead

        if lastEven is not None:
            lastEven.next = None

    return head


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


arr = [1, 2, 3, 4, 5, 6]
head = create_linked_list(arr)
print('Before Even After Odd function:')
print(print_linked_list(head))
print('After Even After Odd function:')
head2 = even_after_odd(head)
print(print_linked_list(head2))
