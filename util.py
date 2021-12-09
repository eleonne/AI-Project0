class Actor():
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

# LIFO - Depth First Search
class StackFrontier():
    def __init__(self):
        self.frontier = []
        self.explored = []

    def add(self, node):
        self.frontier.append(node)

    def addExplored(self, node):
        self.explored.append(node)

    def contains_state(self, state):
        return any(node.state.id == state.id for node in self.frontier)

    def contains_explored_state(self, state):
        return any(node.state.id == state.id for node in self.explored)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

# FIFO - breadth-first search
class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
