"""
Time Complexity:

1) Building a max-heap takes O(n)
Source: https://www.youtube.com/watch?v=XZ_Beap6Vo0
Explanation:
If array has n elements, max nodes at height h is (n/(2^h))
Time complexity for one level is h * num_of_nodes_at_that_level = `h*(n/(2^h))`
Total number of levels in BinaryTree is log(n) to base 2.

Therefore, total time complexity is:
=> ∑(0->logn) n/(2^h) * O(h)
=> O(n ∑(0->logn) h/(2^h))
=> O(n ∑(0->infinity) h/(2^h)) //upper bound; ∑(0->infinity) h/(2^h) = 2 (wiki)
=> O(n * 2)
=> O(n)

2) Heapify method takes time complexity of O(n logn) for n nodes
Source: http://www.cs.toronto.edu/~krueger/cscB63h/lectures/tut02.txt
-MaxHeapify is recursively called **at most** h times, where h is the
 height of the subtree starting at i
-Each call to MaxHeapify takes c steps, for some constant c

Therefore:
for all inputs, **at most** ch steps are needed where h is the
 height of the subtree starting at i

So, the worst case time complexity is O(h) where h is the subtree with
root i OR O(log n) since h = log n = the height of the entire tree

For n nodes, n * O(h) => O(n logn)

Space Complexity: O(1)
"""


def heapify(arr, n, i):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    TODO: Converts an array (in place) into a maxheap, a complete binary tree
    with the largest values at the top
    """

    # Using i as the index of the current node, find the 2 child nodes
    # (if the array were a binary tree) and find the largest value. If one of
    # the children is larger swap the values and recurse into that subree

    # consider current index as largest
    largest_index = i
    left_node = 2 * i + 1
    right_node = 2 * i + 2

    # compare with left child
    if left_node < n and arr[i] < arr[left_node]:
        largest_index = left_node

    # compare with right child
    if right_node < n and arr[largest_index] < arr[right_node]:
        largest_index = right_node

    # if either of left/right child is the largest node, heapify
    if largest_index != i:
        # swap largest_index with current_index
        arr[i], arr[largest_index] = arr[largest_index], arr[i]
        heapify(arr, n, largest_index)


def heapsort(arr):
    n = len(arr)

    # As a first step, convert the array to max-heap. In this step, we are
    # building a max-heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    # print(arr)

    # Extract elements one-by-one. Remember, we remove a node from root node
    # but this may violate the properties of a Heap. Therefore, we need
    # to heapify
    for i in range(n-1, 0, -1):
        # Swap last element with root node (in otherwords, remove root node)
        arr[i], arr[0] = arr[0], arr[i]
        # Again, this might mess-up the Heap properties. Therefore, Heapify
        heapify(arr, i, 0)


# Tests
def test_function(test_case):
    heapsort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")


arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
test_case = [arr, solution]
test_function(test_case)

arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
test_case = [arr, solution]
test_function(test_case)

arr = [99]
solution = [99]
test_case = [arr, solution]
test_function(test_case)
