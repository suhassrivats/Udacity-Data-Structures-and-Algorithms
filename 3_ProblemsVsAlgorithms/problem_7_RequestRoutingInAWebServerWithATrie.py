# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path, handler=None):
        # Insert the node as before
        self.children[path] = RouteTrieNode(handler)


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = handler

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for path in path_list:
            if path not in node.children:
                node.insert(path)
            node = node.children[path]
        node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        if self.root is None:
            return self.not_found
        node = self.root
        for part in path:
            if part not in node.children:
                return self.not_found
            node = node.children[part]
        return node.handler


class Router:
    def __init__(self, handler=None, not_found=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(handler)
        self.handler = handler
        self.not_found = not_found if not_found != "" or not_found is not None else "HTTP 404 Page Not Found"

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        node = self.root
        path_list = self.split_path(path)
        node.insert(path_list, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        if path == '/':
            return "You Got Root!"
        node = self.root.root
        path_list = self.split_path(path)
        for part in path_list:
            if part not in node.children:
                return "HTTP 404 Page Not Found"
            node = node.children[part]
        if not node.handler:
            return "HTTP 404 Page Not Found"
        return node.handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_list = path.split('/')

        # discard the empty strings
        if path_list[0] == '':
            path_list = path_list[1:]
        if path_list[-1] == '':
            path_list = path_list[:-1]
        return path_list


# ----------------------------------------------------------------------
"""
Here are some test cases and expected outputs you can use to test your
implementation
"""

# create the router and add a route
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/contact", "contact us")  # add a route

# should print 'root handler'
# root handler ('root handler'): You Got Root!
print("\nroot handler ('root handler'):", router.lookup("/"))

# should print 'not found handler' or None if you did not implement one
# /home ('not found handler' or None): HTTP 404 Page Not Found
print("/home ('not found handler' or None):", router.lookup("/home"))

# should print 'about handler'
# /home/about ('about handler'): about handler
print("/home/about ('about handler'):", router.lookup("/home/about"))

# should print 'about handler' or None if you did not handle trailing slashes
# /home/about/ ('about handler' or None): about handler
print("/home/about/ ('about handler' or None):", router.lookup("/home/about/"))

# should print 'not found handler' or None if you did not implement one
# /home/about/me ('not found handler' or None): HTTP 404 Page Not Found
print("/home/about/me ('not found handler' or None):",
      router.lookup("/home/about/me"))

# /home/contact ('contact us'): contact us
print("/home/contact ('contact us'):", router.lookup("/home/contact/"))


# another test...
rout1 = Router("handle this", "")
rout1.add_handler("/something", "something handler")
rout1.add_handler("/something/somewhere", "somewhere handler")

# /home (not found): HTTP 404 Page Not Found
print("\n/home (not found):", rout1.lookup("/home"))

# /something ('something handler'): something handler
print("/something ('something handler'):", rout1.lookup("/something/"))

# /something/somewhere ('somewhere handler'): somewhere handler
print("/something/somewhere ('somewhere handler'):",
      rout1.lookup("/something/somewhere"))
print()


# Reference: https://github.com/ssi112/data-structures-algorithms/blob/master/project3/7_problem.py
