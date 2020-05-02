# Explanation_3: Rearrange Array Digits

**Requirements:**

Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is `O(nlog(n))`.

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.



**Approach:**

We know that a maximum number can be formed from given digits (0-9) when the largest digit appears first, second largest digit appears second, and so on.. finally the smallest digit appears in the end. We can extend the same logic to solve this problem. We start by sorting the specified array in descending order and construct two numbers (say x and y) by picking alternating digits from the array i.e. x is filled with digits at the odd indices and y is filled with digits at the even indices of the sorted array.



**Complexity Analysis:**

*Time complexity:*

- Sorting: `O(nlog(n))` // for using mergesort
- 2-for loops: `O(n/2 + n/2)` => `O(n)` // iterating with the step-size of 2 makes it n/2
- Total: `O(nlogn + n)` => `O(nlog(n))`

*Space complexity:*

- Input space: `O(n)` where `n` is the length of input list
- Auxiliary space (extra or temporary space): `O(1)` // since we are reversing the sorted input in-place
- Total: Input space + Auxiliary space => `O(n + 1)` => `O(n)`
