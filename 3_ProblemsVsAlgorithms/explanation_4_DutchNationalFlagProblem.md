# Explanation_4: Dutch National Flag Problem

**Requirements:**

Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.



**Approach:**

To keep the `1`s in its position as it is and move all `0`s and `2` to left and right respectively. This is an in-place algorithm which uses no extra space.

Although I could use other approach which is to scan through the entire list and store the count of 0, 1, and, 2 in a dictionary. Then print it in a sorted order. This would give the same time complexity as my above approach but we would have to use extra space for dictionary and sorted array. 

So the trade-off here really is space. Therefore, I decided to use in-place algorithm in this case.



**Complexity Analysis:**

- *Time complexity:* `O(n)` // visiting every element in the array
- *Space complexity:*
  - Input space => `O(n)`
  - Auxiliary space => `O(1)`
  - Total space => `O(n + 1)` => `O(n)`

