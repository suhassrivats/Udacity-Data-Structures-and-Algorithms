
# MergeSort

MergeSort is a *divide and conquer* algorithm that divides a list into equal halves until it has two single elements and then merges the sub-lists until the entire list has been reassembled in order.

### Divide
Our MergeSort code will focus first on the divide portion of the algorithm. If the list we receive has only a single element in it, the list can be considered sorted and we can return immediately.  This is our recursion base case.  If we have more than 1 element we need to split the list into equal halves and call MergeSort again for each half.

### Conquer
Once you have split the list down to single elements, your mergesort will start merging lists, in order, until you have reassembled the entire list in order.

## Design

First, let's sketch this out. It's clear we want a recursive function, but how will it govern its recursion?

```python
def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items
    
    # Otherwise, find the midpoint and split the list
    # TODO
    # left =
    # right =
    
    # Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)
    
    # Merge our two halves and return
    return merge(left, right)
    
def merge(left, right):
    # Given two ordered lists, merge them together in order,
    # returning the merged list.
    # TODO
```

We have decomposed the problem, now we will address each piece separately.

### Divide

We can use python's `//` operator to find a midpoint. If `items`'s length is even, we will have the midpoint. If `items`'s length is odd, we will have one half larger by one.


```python
list1 = [0, 1, 2, 3]
midpoint1 = len(list1) // 2
print('List 1 midpoint: {}'.format(midpoint1))

list2 = [4, 5, 6]
midpoint2 = len(list2) // 2
print('List 2 midpoint: {}'.format(midpoint2))
```

    List 1 midpoint: 2
    List 2 midpoint: 1


With our midpoints, we can slice the lists using python's special notation. Note, you can improve effencncy by not using the slice function. Instead, keep track of indicies.


```python
left1 = list1[:midpoint1]
right1 = list1[midpoint1:]
print('List 1 left side: {}'.format(left1))
print('List 1 right side: {}'.format(right1))

left2 = list2[:midpoint2]
right2 = list2[midpoint2:]
print('List 2 left side: {}'.format(left2))
print('List 2 right side: {}'.format(right2))
```

    List 1 left side: [0, 1]
    List 1 right side: [2, 3]
    List 2 left side: [4]
    List 2 right side: [5, 6]


That addresses our first TODO, now for the fun one.

The `merge` function needs to take two sorted lists, and interleave them, yielding a _merged_ sorted list. We can accomplish that by tracking an index into both lists, and once one is exhausted, appending the remaining items from the other list.


```python
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Move through the lists until we have exhausted one
    while left_index < len(left) and right_index < len(right):
        # If left's item is larger, append right's item
        # and increment the index
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        # Otherwise, append left's item and increment
        else:
            merged.append(left[left_index])
            left_index += 1
     
    # Append any leftovers. Because we've broken from our while loop,
    # we know at least one is empty, and the remaining:
    # a) are already sorted
    # b) all sort past our last element in merged
    merged += left[left_index:]
    merged += right[right_index:]
        
    # return the ordered, merged list
    return merged

# Test this out
merged = merge([0, 1,3,7], [2,5,6])
print(merged)
```

    [0, 1, 2, 3, 5, 6, 7]


Now we can combine our TODO resolutions into our sketch from above.


```python
def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged


test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
print('{} to {}'.format(test_list_3, mergesort(test_list_3)))
```

    [8, 3, 1, 7, 0, 10, 2] to [0, 1, 2, 3, 7, 8, 10]
    [1, 0] to [0, 1]
    [97, 98, 99] to [97, 98, 99]



```python

```
