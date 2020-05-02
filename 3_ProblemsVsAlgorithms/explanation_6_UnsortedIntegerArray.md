# Explanation_6: Unsorted Integer Array

**Requirement:**

Look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.



**Approach:**

Initially assume that `min` and `max` values are the first element of the array. Use linear search algorithm to check if the current element is greater/lesser than min/max values. Update them accordingly and return (min, max) values in a tuple format.



**Complexity Analysis:**

*Time complexity*  => `O(n)` // iterate through each item in an array

*Space complexity:*

- Input space => `O(n)`
- Auxiliary space => `O(1)`
- Total space => `O(n + 1)`  => `O(n)`