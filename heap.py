class Heap:

    def __init__(self):
        self.root_node = None

    def peek(self):
        return self.root_node

    def insert(self, value):
        if self.root_node is None:
            self.root_node = Node(value)


class Node:

    def __init__(self, val):
        self.value = val
        self.parent = None
        self.left_child = None
        self.right_child = None
