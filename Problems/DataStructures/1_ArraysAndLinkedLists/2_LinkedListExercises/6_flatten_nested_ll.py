"""
Flattening a nested linked list:
Suppose you have a linked list where the value of each node is a sorted linked
list (i.e., it is a nested list). Your task is to flatten this nested
list—that is, to combine all nested lists into a single (sorted) linked list.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)


def merge(list1, list2):
    """
    Implement this function so that it merges the two linked lists in a
    single, sorted linked list.
    """
    merged = LinkedList(None)

    # If either of the linked lists are None, then return the other.
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    p = list1.head
    q = list2.head

    while p or q:
        if p is None:
            merged.append(q)
            q = q.next
        elif q is None:
            merged.append(p)
            p = p.next
        elif p.value <= q.value:
            merged.append(Node(p))
            p = p.next
        else:
            merged.append(Node(q))
            q = q.next

    return merged


class NestedLinkedList(LinkedList):
    def flatten(self):
        """
        Implement this method to flatten the linked list in ascending
        sorted order.
        """
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))

########## TESTS #############
# First Test scenario. Here's some code that will generate a nested linked
# list that we can use to test the solution:
# linked_list = LinkedList(Node(1))
# linked_list.append(Node(3))
# linked_list.append(Node(5))

# nested_linked_list = NestedLinkedList(Node(linked_list))

# second_linked_list = LinkedList(Node(2))
# second_linked_list.append(4)

# nested_linked_list.append(Node(second_linked_list))


linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

merged = merge(linked_list, second_linked_list)
node = merged.head
while node is not None:
    # This will print 1 2 3 4 5
    print(node.value)
    node = node.next
print('*' * 10)

# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
while node is not None:
    # This will print 1 2 3 4 5
    print(node.value)
    node = node.next

print('*' * 5, 'Flattened LinkedList', '*' * 5)
nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)
flattened = nested_linked_list.flatten()

node = flattened.head
while node is not None:
    # This will print 1 2 3 4 5
    print(node.value)
    node = node.next
