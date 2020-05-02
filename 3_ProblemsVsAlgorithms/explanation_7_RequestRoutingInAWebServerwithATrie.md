# Explanation_7: Request Routing in a Web Server with a Trie

**Requirement:**

Implement a [HTTPRouter](https://github.com/suhassrivats/Udacity-Data-Structures-and-Algorithms/blob/master/3_ProblemsVsAlgorithms/HTTPRouterUsingATrie.md) like you would find in a typical web server using the Trie data structure.



**Approach:**

It is described in [HTTPRouter](https://github.com/suhassrivats/Udacity-Data-Structures-and-Algorithms/blob/master/3_ProblemsVsAlgorithms/HTTPRouterUsingATrie.md).



**Complexity Analysis:**

*Time complexity:*

- Insert: `O(n)` where n is length of input path. Every character of the path must be evaluated in order to split the path into segments. In worst case, number of segments can grow linearly with length of path, and every segment has to be added to a dictionary. Adding to a dictionary has O(1) time.
- Find: `O(m)`where m is length of the list of path segments.

*Space complexity:*

- Insert: `O(n)` where n length of input path. We store all path segment strings in the trie nodes (not using any kind of hashing) so the space requirement grows even if there is only one path segment. We could possibly reduce this to O(m) where m is number of path segments if we stored hashes of the segments instead of segments themselves.
- Find: `O(n)` where n is length of input.