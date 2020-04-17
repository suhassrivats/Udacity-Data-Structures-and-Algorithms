"""
Implement a stack using a linked list
Previously, we looked at how to implement a stack using an array. While that
approach does work, we saw that it raises some concerns with time complexity.
For example, if we exceed the capacity of the array, we have to go through the
laborious process of creating a new array and moving over all the elements
from the old array.

What if we instead implement the stack using a linked list? Can this improve
our time complexity? Let's give it a try.
"""


class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            # place the new node at the head (top) of the linked list
            new_node.next = self.head
            self.head = new_node

        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return

        value = self.head.value  # copy data to a local variable
        # move head pointer to point to next node (top is removed by doing so)
        self.head = self.head.next
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0
