## Explanation_1: LRU Cache

**Requirement:**

The lookup operation i.e., `get()` and `put()` / `set()` is supposed to be fast for a cache memory. All operations should take `O(1)`.

**Summary:**

In order to achieve this, I have used two data structures:

- `Hashtable`
  - It offers a constant lookup time
- `Doubly Linked List`
  - For a doubly linked list, it's constant time to add/remove a node if we know the address of a node.

**Time and Space Complexity:**

*Time Complexity:*

I am combining the constant lookup feature of a `Hashtable` with a `DoublyLinkedList`. The idea is that the dictionary value will store the address of a DoublyLinkedList (DLL) Node.  We can then perform add/remove operations on a DLL in constant time. Thereby making all operations (such as lookup, add/remove nodes) constant time `O(1)`



*Space Complexity:*  

Space complexity is the sum of `Input Size` + `Auxillary Space`

1. Input space:

   - Dictionary space: `O(n)`

   - Doubly Linked List space: `O(n)`

   - Total Input space: `O(n + n)` => `O(n)`

2. Auxiliary Space:

It is the temporary space (excluding the input size) allocated by your algorithm to solve the problem, with respect to input size. For example, initialization of loops, function call, print, return statements etc. are all part of Auxiliary space.

Let us say auxiliary operations for this algorithm takes 4 bytes which is a constant space =>  `O(1)`

3. Total Space Complexity => `Input Size` + `Auxillary Space`  => `O(n + 1)` => `O(n)`
