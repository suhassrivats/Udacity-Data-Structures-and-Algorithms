# Explanation_3: Huffman Coding

**Requirement:**

Implement encoding and decoding algorithms using Huffman coding which is a lossless schema.

**Summary:**

[Detailed explanation here](https://medium.com/iecse-hashtag/huffman-coding-compression-basics-in-python-6653cdb4c476)

The concept behind Huffman Coding is that there has to be fewer bits assigned for frequently occurring letters and more bits for less frequent ones.

`huffnam_encoding`:

- First, for a given string I will find the frequency of each character and store it in a dictionary.
- I will then construct a heap using Python's `heapq` module.
- We build a Huffman Tree using the constructed heap where we will join two lowest value nodes until we have a root node.
- We then add `0` all left branches and `1` to all right branches.
- We encode the given text based on these values and send `encoded_text` and heap`tree` to `huffman_decode` function.

![img](https://miro.medium.com/max/2460/1*XtlW_qVfhRMyXJQIxn4Obw.png)

`huffman_decoding`:

Based on the tree and encoded_text we can decode it and retrieve the original string.

**Time and Space Complexity:**

*Time Complexity:*

- `O(n)`: iterate through the string and store its character and frequency in a dictionary

- `O(n)`: the list comprehension and heapify commands will take `O(n + logn)` => `O(n)`

```python
heap = [[frequency, [symbol, '']] for symbol, frequency in huff.items()]  # O(n)
heapq.heapify(heap)  # O(logn)
```

- `O(n)`: within the while loop which takes `O(n)` time:
  - left, right - heappop operation takes constant time `O(1 + 1)` => `O(1)`
  - let us say that the length of a list named `value` is `v`, appending `0` or `1` to `value[1]` is a constant operation. Therefore, the two for loops take `2 * O(v * 1)` => `O(v)`. Since `v` is of a constant length, we can consider it a constant => `O(1)`
  - heappush is a constant operation => `O(1)`
  - Time complexity of the while loop is `O(n * (1+1+1))` => `O(n*3)` => `O(n)`

```python
while len(heap) > 1:
        left = heapq.heappop(heap)  # O(1)
        # print('left = ', left)
        right = heapq.heappop(heap)
        # print('right = ', right)

        # Add `0` to left and `1` to right
        for value in left[1:]:  # O(v)
            value[1] = '0' + value[1]  # O(1)
        # print('left add 0 =', left)
        for value in right[1:]:
            value[1] = '1' + value[1]
        # print('right add 1 =', right, '\n')

        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])  #(1)
```

- `O(n)`: For code outside the while loop it takes linear time.

```python
# Make a dictionary of a char and its binary code
huffman_list = right[1:] + left[1:] # O(1)
global huffman_dict
huffman_dict = {a[0]: str(a[1]) for a in huffman_list} # O(n)

huffcode = encoded_text(huffman_dict, data) # O(n) -- for loop inside this function

return huffcode, heap
```

- Total time complexity (encoding) => `O(n) + O(n) + O(n) + O(n)` => `O(4n)` => `O(n)`

- Similarly, total time complexity for decoding => `O(n)`



*Space Complexity:*

- It takes `O(distinct_characters)` space for huffman encoding and decoding to store encoded/decoded data.
