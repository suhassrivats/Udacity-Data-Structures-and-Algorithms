
# Knapsack Problem
Now that you saw the dynamic programming solution for the knapsack problem, it's time to implement it. Implement the function `max_value` to return the maximum value given the items (`items`) and the maximum weight of the knapsack (`knapsack_max_weight`). The `items` variable is the type `Item`, which is a [named tuple](https://docs.python.org/3/library/collections.html#collections.namedtuple).


```python
import collections

Item = collections.namedtuple('Item', ['weight', 'value'])


def max_value(knapsack_max_weight, items):
    """
    Get the maximum value of the knapsack.
    """
    pass



tests = [
    {
        'correct_output': 14,
        'input':
            {
                'knapsack_max_weight': 15,
                'items': [Item(10, 7), Item(9, 8), Item(5, 6)]}},
    {
        'correct_output': 13,
        'input':
            {
                'knapsack_max_weight': 25,
                'items': [Item(10, 2), Item(29, 10), Item(5, 7), Item(5, 3), Item(5, 1), Item(24, 12)]}}]
for test in tests:
    assert test['correct_output'] == max_value(**test['input'])
```

<span class="graffiti-highlight graffiti-id_sczu399-id_vljhmf7"><i></i><button>Hide Solution</button></span>


```python
def max_value(knapsack_max_weight, items):
    lookup_table = [0] * (knapsack_max_weight + 1)

    for item in items:
        for capacity in reversed(range(knapsack_max_weight + 1)):
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)

    return lookup_table[-1]
```
