# Explanation_1: Square Root of An Integer

**Requirement:**

To find the square root of an integer in `O(log(n))` time complexity without using any Python library.



**Summary:**

**Naïve Approach:** 

To find the floor of the Square Root, try with all natural numbers starting from 1. Continue to increment the number by 1 until the product of the that number with itself is greater than input number.

Complexity Analysis:

- *Time complexity* => `O(sqrt(n))`
- *Space complexity:*
  - Input space => `O(1)`
  - Auxiliary space => `O(1)`
  - Total space => `O(1 + 1)` => `O(2)` => `O(1)`

**Optimized Approach:**

In the Naïve approach, we are trying to find square root of a number by multiplying a natural number by itself (starting from 1, increment by 1). This was further optimized using Binary Search Algorithm.

Complexity Analysis:

- *Time complexity:* `O(log(n))` as the time-complexity is dominated by BinarySearch
- *Space complexity:*
  - Input space: `O(1)` as input is a constant (integer)
  - Auxiliary space (extra or temp): `O(1)` 
  - Total space: `O(1 + 1)` => `O(2)` => `O(1)`