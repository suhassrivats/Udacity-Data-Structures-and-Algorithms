# Explanation_7: Request Routing in a Web Server with a Trie

**Requirement:**

Implement a [HTTPRouter](https://github.com/suhassrivats/Udacity-Data-Structures-and-Algorithms/blob/master/3_ProblemsVsAlgorithms/HTTPRouterUsingATrie.md) like you would find in a typical web server using the Trie data structure.



**Approach:**

It is described in [HTTPRouter](https://github.com/suhassrivats/Udacity-Data-Structures-and-Algorithms/blob/master/3_ProblemsVsAlgorithms/HTTPRouterUsingATrie.md).



**Complexity Analysis:**

*Time complexity:*

The worst-case runtime for creating a trie is a combination of `m`, the length of the longest key in the trie, and `n`, the total number of keys in the trie. Thus, the worst case runtime of creating a trie is `O(mn)`.

The time complexity of searching, inserting, and deleting from a trie depends on the length of the word a that’s being searched for, inserted, or deleted, and the number of total words, `n`, making the runtime of these operations `O(an)`. Of course, for the longest word in the trie, inserting, searching, and deleting will take more time and memory than for the shortest word in the trie.

Reference:
https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014

*Space complexity:*

Splitting a string to store individual parts of the path is dependent on the length of the string and the depth or level of the path, which could be quite large on a site with many pages. In any case, using a dictionary should be `O(n)` where n is the count or number of components in the path.