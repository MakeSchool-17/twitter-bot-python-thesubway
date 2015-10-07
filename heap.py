class Heap:

    def __init__(self):
        self.root_node = None
        self.num_nodes = 0

    def peek(self):
        return self.root_node

    def insert(self, value):
        new_node = Node(value)
        if self.root_node is None:
            self.root_node = new_node
            return self.root_node
        current_node = self.root_node
        while current_node is not None:
            if current_node.value[0] == value[0]:
                current_node.value = (current_node.value[0], current_node.value[1] + 1)
                return None
            elif value > current_node.value:
                if current_node.left_child is None:
                    current_node.left_child = new_node
                    return new_node
                current_node = current_node.left_child
            else:
                if current_node.right_child is None:
                    current_node.right_child = new_node
                    return new_node
                current_node = current_node.right_child
        return current_node
        self.num_nodes += 1

    def search(self, value):
        current_node = self.root_node
        while current_node is not None:
            if current_node.value == value:
                return current_node
            if value > current_node.value:
                current_node = current_node.right_child
            else:
                current_node = current_node.left_child
        return current_node
        pass

    def __str__(self):
        lines = []
        current_row = 0
        current_nodes = [self.root_node]
        while True:
            # use formula for current row
            # num_elements = 2 ^ current_row
            next_nodes = []
            new_row_exists = False
            for each_node in current_nodes:
                if each_node is None:
                    print("here")
                    next_nodes.append(None)
                    # next_nodes.append(Node((-1, -1)))
                else:
                    next_nodes.append(each_node.left_child)
                    next_nodes.append(each_node.right_child)
                    new_row_exists = True
            if new_row_exists is False:
                break
            lines.append(current_nodes)
            current_nodes = next_nodes
            current_row += 1
        return str(lines)


class Node:

    def __init__(self, val):
        self.value = val
        # self.parent = None
        self.left_child = None
        self.right_child = None

    # def add_child(self, child_node):
    #     # step 1, get it to the furthest node possible:
    #     if self.left_child is None and self.right_child is None:
    #         self.left_child = child_node
    #     elif self.left_child is not None and self.right_child is None:
    #         if child_node.value >= self.left_child.value:
    #             self.right_child = child_node
    #         else:
    #             self.right_child = self.left_child
    #             self.left_child = child_node

if __name__ == '__main__':
    my_heap = Heap()
    my_heap.insert(("3", 3))
    print(my_heap.root_node.value)
    my_heap.insert(("5", 5))
    my_heap.insert(("1", 1))
    my_heap.insert(("2", 2))
    my_heap.insert(("4", 4))
    print(my_heap.root_node.left_child.value)
    print(my_heap.root_node.right_child.value)
    print(my_heap.root_node.right_child.left_child.value)
    print(my_heap.root_node.left_child.right_child.value)
    print(my_heap)
