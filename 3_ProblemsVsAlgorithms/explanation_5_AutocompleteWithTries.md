# Explanation_5: Autocomplete with Tries

**Requirement:**

To implement the autocomplete feature for words using `Trie` datastructure. For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]`



**Approach:**

Implement a `Trie` datastructure with `insert` word, `find` prefix and, `match` prefix functionalities.  find_words function will find all words in a given prefix and return all matching words in a list format.



**Complexity Analysis:**

*Time complexity:*

- Insert => `O(n)` where `n` is the length of the word
- Find => `O(s)` where `s` is the length of the search string
- Find_words => `O(t)` where `t` is the number of nodes in the trie. In the worst case, let us say when the search string is empty, we have to visit every node to build matching results (i.e., return all words).

*Space complexity:*

- Insert => `O(n)` where `n` is the total number of nodes in a Trie. Initially, we expect Trie space to grow linearly with the input number of words but it will gradually decrease as new words are likely to overlap with the existing nodes.
- Find_words => `O(n)` where `n` is the number of nodes in a Trie. For instance, if all words in a dictionary are starting with `a` and search string is also `a` then it has to visit every node which is a linear operation.
