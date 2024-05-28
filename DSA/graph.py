class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.routes_graph_dict = {}

        for start, end in edges:
            if start in self.routes_graph_dict:
                self.routes_graph_dict[start].append(end)
            else:
                self.routes_graph_dict[start] = [end]
        print(self.routes_graph_dict)

    def get_paths(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]

        if start == end:
            return [path]
#       Here, we are trying to address a situation where the person enters his/her starting point
#       as their destination as well, and we want to return the person's starting destination as their
#       path because they do not really go anywhere
        if start not in self.routes_graph_dict:
            return []
#       Here, we are trying to handle a situation whereby the person enters a starting point
#       which we do not recognize as generally being a starting point. For e.g. flight moves from
#       calabar to uyo before going to Abuja but on coming back we can only move from Abuja straight
#       calabar. Hence, if the user enters uyo there will be no route to take them to calabar. Since uyo
#       is not a starting point
        paths = []

        for node in self.routes_graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    # In our main function we have our start and end specified, so when we call our get_path() we can go
    # ahead and pass them as arguments. To create our paths after appending our start in the path
    # initialization above, we check the value of our key 'start' and for each of the value, they are the nodes
    # next we take each node and check if it is in our path, if it isn't we recurse it by calling the
    # get_path() on it, so it takes node as the start. Check video at C:\Users\admin\Pictures\Camera Roll
    # for detailed explanation.

    def get_shortest_path(self, start, end, path=None):
        if path is None:
            path = []

        path = path + [start]

        if start not in self.routes_graph_dict:
            return None
        if start == end:
            return path

        shortest_path = None
        for node in self.routes_graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path
#     What that block of code means is that we take our node check if it isn't already in our
# path and then recurse on it using the get_shortest_path(), we send node as the start
# for every path we receive that's our shortest path hence, we initialize it to sp.
# Since sp can be None, we call the if statement and if shortest path is None, remember that's what
# we initialized it above, we make the sp we just obtained from our recursion our shortest_path
# Also when we obtain a new sp we check if it's length is less than our current shortest_path and if
# it is we make it our new shortest_path, till we finish our recursion. In this example, one output
# is displayed because after we get the length 3, another path with same length doesn't get to replace
# the first one because our code specifies that for it to happen it must have a length less than our current
# shortest path.


if __name__ == '__main__':
    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto')
    ]
    # represents all the edges connecting two nodes, because this might be a little expensive trying
    # to iterate over this tuple everytime we need to carry out an operation. Instead, we can create
    # a dict from the tuple. Where the first node is mapped to a list of nodes which can be navigated
    # to from it. For e.g.  we can go to either Paris or Dubai from Mumbai hence we make Mumbai our
    # key and map ['Dubai' and 'Paris' to it]
    routes_graph = Graph(routes)
    start = 'Mumbai'
    end = 'New York'
    print(routes_graph.get_paths(start,end))
    print(routes_graph.get_shortest_path(start,end))