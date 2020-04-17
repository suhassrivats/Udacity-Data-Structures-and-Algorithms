# Time Complexity Analysis for "Unscramble Computer Science Problems"


## Task0:

This task will take constant time i.e., `O(1)` as the access time for items in a list will take a constant time.

## Task1:

This task will take linear time i.e., `O(n)` as we have to iterate through each line in a list to get phone numbers. Even though there are two for loops (one for texts and another for calls) which will take `O(n+n)` => `O(2n)`, we can round it off to `O(n)`.

## Task2:

- `O(n)`: for the for loop
- `O(n)`: for max items in a list

***Total time complexity*** `O(n+n)` => `O(n)`

## Task3:

PartA:

- `O(n+n)` => `O(2n)` => `O(n)`: for 2 lists
- `O(1)`: for a set.
- `O(n)`: it is obvious that for-loop is linear time.
  - `O(1)`: Within the loop, if each re.search takes `m` operations to search a pattern in a word (`O(m)`), then:
    - if-block will take `O(m^2)` as there are two re.search operations.
    - elif-block will take `O(m+1+1)` => `O(m)` operations.
    - String slicing takes `O(k)`. In this case it is always slicing 4 characters. Therefore, it is `O(4)` ~ `O(1)`.
    - Clearly, `O(m^2)` is slower.
    - <u>*Note:*</u> in practical cases such as this, phone numbers are always of a constant size (10-13 digits). Therefore the re.search operation takes a constant time on a phone number. If m is a constant, then `O(m^2)` => `O(1)`
- `O(n*log(n))`: sorting a list

***Total time complexity*** of this code block is `O(n + 1 + n*1 + nlog(n))` =>  `O(2n+nlogn)` =>  `O(nlog(n))`

PartB:

- `O(n)`: for list comprehension
- `O(1)`: for finding percentage

***Total time complexity:*** `(O(n+1))` => `O(n)`

## Task4:

- `O(n)`: the four list comprehensions take `O(n)` complexity each. `O(4n)` => `O(n)`
- `O(n)`: for loop takes `O(n)` time complexity
- `O(nlogn)`: sorting takes `O(nlogn)` 
- `O(n)`: for loop printing sorted list

***Total time complexity:*** `O(n + n + nlogn + n)` => `O(3n + nlogn)` => `O(nlogn)`
