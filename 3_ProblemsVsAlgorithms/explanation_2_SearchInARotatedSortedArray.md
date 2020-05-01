# Explanation_2: Search in a Rotated Sorted Array

**Requirement:**

Given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

Given a target value to search. If found in the array return its index, otherwise return -1.

We can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`.

Example: Input: `nums = [4,5,6,7,0,1,2], target = 0, Output: 4`



**Approach:**

Find a pivot element (using binary search) such that there are two sorted arrays. Check in which array does the target element reside. Then apply Binary Search on that array to find its position.



**Complexity Analysis:**

*Time complexity:*

- Finding pivot => `O(logn)` // uses BinarySearch
- Binary search => `O(logn)`
- Total: `O(logn + logn)` => `O(log(n))`

*Space complexity:*

- Input space: `O(n)` // array input
- Auxiliary space (extra or temporary space): `O(n)` // for sorted array
- Total: Input space + Auxiliary space => `O(n + n)` => `O(n)`
