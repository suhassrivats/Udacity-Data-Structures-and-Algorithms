
# Dijkstra's Algorithm
In this exercise, you'll implement Dijkstra's algorithm. First, let's build the graph.
## Graph Representation
In order to run Dijkstra's Algorithm, we'll need to add distance to each edge. We'll use the `GraphEdge` class below to represent each edge between a node.


```python
class GraphEdge(object):
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance
```

The new graph representation should look like this:


```python
class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)

class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)
```

Now let's create the graph.


```python
node_u = GraphNode('U')
node_d = GraphNode('D')
node_a = GraphNode('A')
node_c = GraphNode('C')
node_i = GraphNode('I')
node_t = GraphNode('T')
node_y = GraphNode('Y')

graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])
graph.add_edge(node_u, node_a, 4)
graph.add_edge(node_u, node_c, 6)
graph.add_edge(node_u, node_d, 3)
graph.add_edge(node_d, node_u, 3)
graph.add_edge(node_d, node_c, 4)
graph.add_edge(node_a, node_u, 4)
graph.add_edge(node_a, node_i, 7)
graph.add_edge(node_c, node_d, 4)
graph.add_edge(node_c, node_u, 6)
graph.add_edge(node_c, node_i, 4)
graph.add_edge(node_c, node_t, 5)
graph.add_edge(node_i, node_a, 7)
graph.add_edge(node_i, node_c, 4)
graph.add_edge(node_i, node_y, 4)
graph.add_edge(node_t, node_c, 5)
graph.add_edge(node_t, node_y, 5)
graph.add_edge(node_y, node_i, 4)
graph.add_edge(node_y, node_t, 5)
```

## Implementation
Using what you've learned, implement Dijkstra's Algorithm to find the shortest distance from the "U" node to the "Y" node. 


```python
import math

def dijkstra(start_node, end_node):
    pass


print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(node_u, node_y)))
```

<span class="graffiti-highlight graffiti-id_6vmf0hp-id_cjtybve"><i></i><button>Hide Solution</button></span>


```python
def dijkstra(start_node, end_node):
    distance_dict = {node: math.inf for node in graph.nodes}
    shortest_path_to_node = {}

    distance_dict[start_node] = 0
    while distance_dict:
        # Pop the shorest path 
        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]
        shortest_path_to_node[current_node] = distance_dict.pop(current_node)

        for edge in current_node.edges:
            if edge.node in distance_dict:
                new_node_distance = node_distance + edge.distance
                if distance_dict[edge.node] > new_node_distance:
                    distance_dict[edge.node] = new_node_distance
    
    return shortest_path_to_node[end_node]
```
