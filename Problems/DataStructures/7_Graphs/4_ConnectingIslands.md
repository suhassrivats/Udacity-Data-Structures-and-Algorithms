
### Problem Statements

In an ocean, there are `n` islands some of which are connected via bridges. Travelling over a bridge has some cost attaced with it. Find bridges in such a way that all islands are connected with minimum cost of travelling. 

You can assume that there is at least one possible way in which all islands are connected with each other. 

You will be provided with two input parameters:
    
1. `num_islands` = number of islands
    
2. `bridge_config` = list of lists. 
    Each inner list will have 3 elements:
        a. island A
        b. island B
        c. cost of bridge connecting both islands
                       
    Each island is represented using a number
     
**Example:**                       
* `num_islands = 4`
* `bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]`
       
Input parameters explanation:
    1. Number of islands = 4
    2. Island 1 and 2 are connected via a bridge with cost = 1
       Island 2 and 3 are connected via a bridge with cost = 4
       Island 1 and 4 are connected via a bridge with cost = 3
       Island 4 and 3 are connected via a bridge with cost = 2
       Island 1 and 3 are connected via a bridge with cost = 10
       
In this example if we are connecting bridges like this...
* between 1 and 2 with cost = 1
* between 1 and 4 with cost = 3
* between 4 and 3 with cost = 2  

...then we connect all 4 islands with `cost = 6` which is the minimum traveling cost.


### Hint

In addition to using a graph, you may want to use a custom priority queue for solving this problem.

If you do not want to create a custom priority queue, you can use Python's `heapq` implementation.

Using the `heapq` module, you can convert an existing list of items into a heap. The following two functionalities can be very handy for this problem:

1. `heappush(heap, item)` — add `item` to the `heap`
2. `heappop(heap)` — remove the smallest item from the `heap`

Let's look at the above methods in action. We start by creating a list of integers.

### `heappush`


```python
# initialize an empty list 
heap = list()

# insert 5 into heap
heapq.heappush(heap, 6)

# insert 6 into heap
heapq.heappush(heap, 6)

# insert 2 into heap
heapq.heappush(heap, 2)

# insert 1 into heap
heapq.heappush(heap, 1)

# insert 9 into heap
heapq.heappush(heap, 9)

print("After pushing, heap looks like: {}".format(heap))
```

    After pushing, heap looks like: [1, 2, 6, 6, 9]


### `heappop`


```python
# pop and return smallest element from the heap
smallest = heapq.heappop(heap)   

print("Smallest element in the original list was: {}".format(smallest))

print("After popping, heap looks like: {}".format(heap))
```

    Smallest element in the original list was: 1
    After popping, heap looks like: [2, 6, 6, 9]


### `heappush` and `heappop` for items with multiple entries

Note: If you insert a tuple inside the heap, the element at 0th index of the tuple is used for comparision



```python
heap = list()

heapq.heappush(heap, (0, 1))

heapq.heappush(heap, (-1, 5))

heapq.heappush(heap, (2, 0))

heapq.heappush(heap, (5, -1))

print("After pushing, now heap looks like: {}".format(heap))
```

    After pushing, now heap looks like: [(-1, 5), (0, 1), (2, 0), (5, -1)]



```python
# pop and return smallest element from the heap
smallest = heapq.heappop(heap)   

print("Smallest element in the original list was: {}".format(smallest))

print("After popping, heap looks like: {}".format(heap))
```

    Smallest element in the original list was: (-1, 5)
    After popping, heap looks like: [(0, 1), (5, -1), (2, 0)]


Now that you know about `heapq`, you can use it to solve the given problem. You are also free to create your own implementatin of Priority Queues.

Write code in the following function to find and return the minimum cost required to travel all islands via bridges.


```python
def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    TODO complete this method to returh minimum cost of connecting all islands
    """
    pass
```

<span class="graffiti-highlight graffiti-id_07rfocu-id_sgw589w"><i></i><button>Hide Solution</button></span>


```python
# Solution

# The following Solution makes use of one of Python's PriorityQueue implementation (heapq)
# For more details - https://thomas-cokelaer.info/tutorials/python/module_heapq.html
import heapq
def create_graph(num_islands, bridge_config):
    """
    Helper function to create graph using adjacency list implementation
    """
    adjacency_list = [list() for _ in range(num_islands + 1)]
    
    for config in bridge_config:
        source = config[0]
        destination = config[1]
        cost = config[2]
        adjacency_list[source].append((destination, cost))
        adjacency_list[destination].append((source, cost))

    return adjacency_list

def minimum_cost(graph):
    """
    Helper function to find minimum cost of connecting all islands
    """
    
    # start with vertex 1 (any vertex can be chosen)
    start_vertex = 1
    
    # initialize a list to keep track of vertices that are visited
    visited = [False for _ in range(len(graph) + 1)]
    
    # initialize starting list - (edge_cost, neighbor)
    heap = [(0, start_vertex)]
    total_cost = 0

    while len(heap) > 0:
        cost, current_vertex = heapq.heappop(heap)
        
        # check if current_vertex is already visited
        if visited[current_vertex]:
            continue

        # else add cost to total-cost
        total_cost += cost

        for neighbor, edge_cost in graph[current_vertex]:
            heapq.heappush(heap, (edge_cost, neighbor))

        # mark current vertex as visited
        visited[current_vertex] = True

    return total_cost

def get_minimum_cost_of_connecting(num_islands, bridge_config):
    graph = create_graph(num_islands, bridge_config)
    return minimum_cost(graph)
```


```python
def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")
```


```python
num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
solution = 6

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
```

    Pass



```python
num_islands = 5
bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
solution = 13

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
```

    Pass



```python
num_islands = 5
bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
solution = 31

test_case = [num_islands, bridge_config, solution]
test_function(test_case)
```

    Pass

