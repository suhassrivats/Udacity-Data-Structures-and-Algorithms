# Helper Code


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

    # def reverse(self):
    #     """
    #     Reverse the inputted linked list

    #     Args:
    #        linked_list(obj): Linked List to be reversed
    #     Returns:
    #        obj: Reveresed Linked List
    #     """

    #     prev = None
    #     next = None
    #     current = self.head

    #     while current is not None:
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next

    #     self.head = prev

    # def printList(self):
    #     temp = self.head
    #     while(temp):
    #         print(temp.value)
    #         temp = temp.next


def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    rev_linked_list = LinkedList()
    prev = None

    for value in linked_list:
        # This is a new node
        new_node = Node(value)
        new_node.next = prev
        prev = new_node
    rev_linked_list.head = prev

    return rev_linked_list


# Tests
llist = LinkedList()
for value in [4, 2, 5, 1, -3, 0]:
    llist.append(value)
print(llist)

flipped = reverse(llist)
print(flipped)
is_correct = list(flipped) == list(
    [0, -3, 1, 5, 2, 4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")

# llist = LinkedList()
# llist.append(20)
# llist.append(4)
# llist.append(15)
# llist.append(85)

# print("Given Linked List")
# llist.printList()
# llist.reverse()
# print("\nReversed Linked List")
# llist.printList()
