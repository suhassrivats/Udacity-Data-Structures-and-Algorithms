# Explanation_2: Search in a Rotated Sorted Array

**Requirement:**

Given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

Given a target value to search. If found in the array return its index, otherwise return -1.

We can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`.

Example: Input: `nums = [4,5,6,7,0,1,2], target = 0, Output: 4`



**Approach:**

Find a pivot element (using binary search) such that there are two sorted arrays. Check in which array does the target element reside. Then apply Binary Search on that array to find its position.



**Complexity:**

- *Time complexity:*
  - Finding pivot => `O(log(n))`
  - Binary Search => `O(log(n))`
  - Total => `O(log(n) + log(n))` => `O(2log(n))` => `O(log(n))`
- *Space complexity:*
          Input space: `O(n)` //for input_list
          Auxiliary space: `O(1)`
          Total space: `O(n + 1)` => `O(1)`