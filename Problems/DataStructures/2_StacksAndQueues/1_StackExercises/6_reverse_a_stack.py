"""
Reverse a stack
If your stack initially has 1, 2, 3, 4 (4 at the top and 1at the bottom),
after reversing the order must be 4, 3, 2, 1 (4 at the bottom
and 1 at the top).
"""


class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def reverse_stack(stack):
    """
    Reverse a given input stack

    Args:
       stack(stack): Input stack to be reversed
    Returns:
       stack: Reversed Stack
    """

    rev_stack = Stack()
    for ele in range(stack.num_elements):
        rev_stack.push(stack.pop())

    return rev_stack


# Alternate method
# def reverse_stack(stack):
#     holder_stack = Stack()
#     while not stack.is_empty():
#         popped_element = stack.pop()
#         holder_stack.push(popped_element)
#     _reverse_stack_recursion(stack, holder_stack)


# def _reverse_stack_recursion(stack, holder_stack):
#     if holder_stack.is_empty():
#         return
#     popped_element = holder_stack.pop()
#     _reverse_stack_recursion(stack, holder_stack)
#     stack.push(popped_element)


# Tests
def test_function(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)

    reverse_stack(stack)
    index = 0
    while not stack.is_empty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")


test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)

test_case_2 = [1]
test_function(test_case_2)
