class Heap:

    def __init__(self):
        self.root_node = None
        self.num_nodes = 0

    def peek(self):
        return self.root_node

    def insert(self, value):
        new_node = Node(value)
        if self.root_node is None:
            self.root_node = Node(value)
        else:
            if value < self.root_node:
                self.root_node.add_child(new_node)
        self.num_nodes += 1


class Node:

    def __init__(self, val):
        self.value = val
        # self.parent = None
        self.left_child = None
        self.right_child = None

    def add_child(self, child_node):
        if self.left_child is None and self.right_child is None:
            self.left_child = child_node
        elif self.left_child is not None and self.right_child is None:
            if child_node.value >= self.left_child.value:
                self.right_child = child_node
            else:
                self.right_child = self.left_child
                self.left_child = child_node

if __name__ == '__main__':
    my_heap = Heap()
    my_heap.insert(1)
    print(my_heap.root_node.value)
