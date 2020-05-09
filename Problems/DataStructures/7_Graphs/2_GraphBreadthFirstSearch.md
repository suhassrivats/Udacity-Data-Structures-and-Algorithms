
# Graph Breadth First Search
In this exercise, you'll see how to do a breadth first search on a graph. To start, let's create a graph class in Python.


```python
class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []
        
    def add_child(self,new_node):
        self.children.append(new_node)
    
    def remove_child(self,del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):
    def __init__(self,node_list):
        self.nodes = node_list
        
    def add_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)
            
    def remove_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)
```

Now let's create the graph.


```python
nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] ) 
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)
```

## Implement BFS
Using what you know about BFS for trees and DFS for graphs, let's do BFS for graphs. Implement the `bfs_search` to return the `GraphNode` with the value `search_value` starting at the `root_node`.


```python
def bfs_search(root_node, search_value):
    pass
```

<span class="graffiti-highlight graffiti-id_fg1wpq1-id_g7fi7m5"><i></i><button>Hide Solution</button></span>


```python
def bfs_search(root_node, search_value):
    visited = []
    queue = [root_node]
    
    while len(queue) > 0:
        current_node = queue.pop(0)
        queue.append(current_node)

        if current_node.value == search_value:
            return current_node

        for child in current_node.children:
            if child not in visited:
                queue.append(child)
```

### Tests


```python
assert nodeA == bfs_search(nodeS, 'A')
assert nodeS == bfs_search(nodeP, 'S')
assert nodeR == bfs_search(nodeH, 'R')
```
