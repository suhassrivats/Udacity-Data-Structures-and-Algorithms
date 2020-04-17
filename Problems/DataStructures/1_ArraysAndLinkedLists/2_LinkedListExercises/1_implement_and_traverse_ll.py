"""
1 - Implementing a simple linked list
* Create a `Node` class with `value` and `next` attributes
* Use the class to create the `head` node with the value `2`
* Create and link a second node containing the value `1`
* Try printing the values (`1` and `2`) on the nodes you created (to make
sure that you can access them!)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(2)
second = Node(1)
head.next = second

print(head.value)
print(second.value)
print('*' * 10)


"""
2 - Extend the linked list
At this point, our linked list looks like this:
2 -> 1
Our goal is to extend it until it looks like this:
2 -> 1 -> 4 -> 3 ->

To do this, we need to create three more nodes, and we need to attach each
one to the `next` attribute of the node that comes before it. Notice that we
don't have a direct reference to any of the nodes other than the `head` node!

See if you can write the code to finish creating the above list:
* Add three more nodes to the list, with the values `4`, `3`, and `5`
"""


head = Node(2)
second = Node(1)
third = Node(4)
fourth = Node(3)
fifth = Node(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

print(head.value)
print(second.value)
print(third.value)
print(fourth.value)
print(fifth.value)
print('*' * 10)


"""
3 - Traversing the list
OK, great! We successfully created a simple linked list. But printing all the
values like we did above was pretty tedious. What if we had a list with
1,000 nodes?

Let's see how we might traverse the list and print all the values, no matter
how long it might be.
"""


current_node = head

while current_node is not None:
    print(current_node.value)
    current_node = current_node.next
print('*' * 10)


"""
4 - Creating a linked list using iteration
Previously, we created a linked list using a very manual and tedious method.
We called `next` multiple times on our `head` node. Now that we know about
iterating over or traversing the linked list, is there a way we can use that
to create a linked list?

* See if you can write the code for the `create_linked_list` function below
* The function should take a Python list of values as input and return the
`head` of a linked list that has those values
* There's some test code, and also a solution, below—give it a try for
yourself first, but don't hesitate to look over the solution if you get stuck
"""


def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    head = None

    for value in input_list:
        new_node = Node(value)

        if head is None:
            head = new_node
        else:
            current_node = head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node

    return head


def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: " + e)


input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list(input_list)
test_function(input_list, head)
print('*' * 10)


"""
5 - A more efficient solution
In the above solution, creation of linked list takes O(n^2) complexity. It
can be made better by maintaining a tail
"""


def create_linked_list_better(input_list):
    head = None
    tail = None

    # TODO: Implement the more efficient version that keeps track of the tail

    for value in input_list:

        new_node = Node(value)

        if head is None:
            head = new_node
            # when we only have 1 node, head and tail refer to the same node
            tail = head

        else:
            # attach the new node to the `next` of tail
            tail.next = new_node
            # update the tail
            tail = tail.next

    return head


def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: " + e)


input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list_better(input_list)
test_function(input_list, head)
