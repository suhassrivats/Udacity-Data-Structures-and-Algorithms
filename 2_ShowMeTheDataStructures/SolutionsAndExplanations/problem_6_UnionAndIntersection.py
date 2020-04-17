class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    """
    Take in two linked lists and return a linked list that is composed of
    its union
    """
    unions = LinkedList()
    set1 = set()
    set2 = set()

    if llist_1.head is None and llist_2.head is None:
        return None

    current1 = llist_1.head
    while current1 is not None:
        set1.add(current1.value)
        current1 = current1.next

    current2 = llist_2.head
    while current2 is not None:
        set2.add(current2.value)
        current2 = current2.next

    set12 = set1.union(set2)

    for i in set12:
        unions.append(i)

    return unions


def intersection(llist_1, llist_2):
    """
    Take in two linked lists and return a linked list that is composed of
    its intersection
    """
    intersections = LinkedList()
    set1 = set()
    set2 = set()

    if llist_1.head is None and llist_2.head is None:
        return None

    current1 = llist_1.head
    while current1 is not None:
        set1.add(current1.value)
        current1 = current1.next

    current2 = llist_2.head
    while current2 is not None:
        set2.add(current2.value)
        current2 = current2.next

    set12 = set1.intersection(set2)

    if len(set12) == 0:
        return None

    for i in set12:
        intersections.append(i)

    return intersections


# Tests

# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)
print("***Linked Lists Case #1***")
print(linked_list_1)
print(linked_list_2)
print("***Union***")
print(union(linked_list_1, linked_list_2))
print("***Intersection***")
print(intersection(linked_list_1, linked_list_2))

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)
print("\n***Linked Lists Case #2***")
print(linked_list_3)
print(linked_list_4)
print("***Union***")
print(union(linked_list_3, linked_list_4))
print("***Intersection***")
print(intersection(linked_list_3, linked_list_4))

# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)
print("\n***Linked Lists Case #3***")
print("Empty List")
print(linked_list_6)
print("***Union***")
print(union(linked_list_5, linked_list_6))
print("***Intersection***")
print(intersection(linked_list_5, linked_list_6))
