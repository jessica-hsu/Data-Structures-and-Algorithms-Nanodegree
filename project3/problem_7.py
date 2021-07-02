# A RouteTrie will store our routes and their associated handlers
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path):
        # Insert the node as before
        self.children[path] = RouteTrieNode()

class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = handler

    def insert(self, path_pieces, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self.root
        for path in path_pieces:
            #print(path)
            if (path not in current.children):
                current.insert(path) # make a RouteTrieNode for each path piece
            current = current.children[path] # make current node where we just left off (go deeper)
        current.handler = handler # set handler after going thru loop. Should be at deepest node

    def find(self, path_pieces):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current = self.root
        for path in path_pieces:
            if (path not in current.children):
                return None
            current = current.children[path] # go deeper in the RouteTrie
        return current.handler

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(handler)
        self.handler = handler

    def add_handler(self, path_name, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_pieces = self.split_path(path_name)
        # pass all path pieces to RouteTrie
        trie = self.root
        trie.insert(path_pieces, handler)

    def lookup(self, full_path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        if (full_path == "" or full_path == "/"):
            return self.handler
        elif (isinstance(full_path, str) is False):
            return "Please enter a valid path"
        else:
            path_pieces = self.split_path(full_path)
            trie = self.root
            return trie.find(path_pieces)

    def split_path(self, full_path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if (full_path[0] == "/"): # if first char is /, remove it
            full_path = full_path[1:]
        if (full_path[-1] == "/"): # if last char is /, remove it
            full_path = full_path[:-1]
        return full_path.split("/")    

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
# add routes to simulate a personal website for a software engineer
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/contact", "contact handler")  # add a route
router.add_handler("/home/projects", "projects handler")  # add a route
router.add_handler("/home/skills", "skills handler")  # add a route
router.add_handler("/home/projects/project_A", "project A handler")  # add a route
router.add_handler("/home/projects/project_B", "project B handler")  # add a route
router.add_handler("/home/projects/project_C", "project C handler")  # add a route

# edge case: root path
print(router.lookup("/")) # root handler

# edge case: path not found
print(router.lookup("/about")) # None

# edge case: None path
print(router.lookup(None)) # Please enter a valid path

# edge cases: trailing /
print(router.lookup("home/skills/")) # skills handler
print(router.lookup("/home/skills")) # skills handler
print(router.lookup("/home/skills/")) # skills handler

# normal cases
print(router.lookup("/home/about/")) # about handler
print(router.lookup("/home/about////////////")) # None handler
print(router.lookup("/home/projects/")) # projects handler
print(router.lookup("/home/projects/project_C")) # project C handler
print(router.lookup("/home/projects_D/")) # None