class Heap:

    def __init__(self):
        self.nodes = []

    def peek(self):
        return self.nodes[0]

    def insert(self, value):
        new_node = Node(value)
        new_index = len(self.nodes)
        parent_index = int((new_index - 1) / 2)
        self.nodes.append(new_node)
        while new_index >= 1:
            if self.nodes[new_index].value[1] > self.nodes[parent_index].value[1]:
                # switch the new_node and parent_node
                temp_node = self.nodes[parent_index]
                self.nodes[parent_index] = self.nodes[new_index]
                self.nodes[new_index] = temp_node
            else:
                break
            # increment everything for next loop:
            new_index = parent_index
            parent_index = int((parent_index - 1) / 2)

    def search(self, value):
        if len(self.nodes) is 0:
            return None
        idx = 0
        current_node = self.nodes[idx]
        while idx < len(self.nodes):
            current_node = self.nodes[idx]
            if current_node.value[0] == value[0]:
                return current_node
            if value[1] < current_node.value[1]:
                # get left child:
                idx = 2 * (idx) + 1
            else:
                # get right child
                idx = 2 * (idx) + 2
        return None

    def delete_max(self):
        if len(self.nodes) == 0:
            raise ValueError('Heap is empty')
            return
        if len(self.nodes) == 1:
            del self.nodes[0]
            return
        self.nodes[0], self.nodes[-1] = self.nodes[-1], self.nodes[0]
        del self.nodes[-1]
        # now swap with largest child
        idx = 0
        while True:
            go_left = False
            current_node = self.nodes[idx]
            if self.number_children(idx) == 0:
                return self.nodes[idx]
            if self.number_children(idx) == 1:
                if self.nodes[idx * 2 + 1].value[1] > self.nodes[idx].value[1]:
                    self.nodes[idx * 2 + 1], self.nodes[idx] = self.nodes[idx], self.nodes[idx * 2 + 1]
                    go_left = True
                else:
                    return self.nodes[idx]
            else:
                left_child = self.nodes[idx * 2 + 1]
                right_child = self.nodes[idx * 2 + 2]
                left_higher = (left_child.value[1] > current_node.value[1])
                right_higher = (right_child.value[1] > current_node.value[1])
                if left_higher is True and right_higher is True:
                    if (left_child.value[1] >= right_child.value[1]):
                        self.nodes[idx * 2 + 1], self.nodes[idx] = self.nodes[idx], self.nodes[idx * 2 + 1]
                        go_left = True
                    else:
                        self.nodes[idx * 2 + 2], self.nodes[idx] = self.nodes[idx], self.nodes[idx * 2 + 2]
                        go_left = False
                elif left_higher is True and right_higher is False:
                    self.nodes[idx * 2 + 1], self.nodes[idx] = self.nodes[idx], self.nodes[idx * 2 + 1]
                    go_left = True
                elif left_higher is False and right_higher is True:
                    self.nodes[idx * 2 + 2], self.nodes[idx] = self.nodes[idx], self.nodes[idx * 2 + 2]
                    go_left = False
                else:
                    return self.nodes[idx]

    def number_children(self, idx):
        if (idx < len(self.nodes) is False):
            raise ValueError('Node does not exist at index: ' + str(idx))
            return None
        if (idx * 2 + 1) >= len(self.nodes):
            return 0
        if (idx * 2 + 2) >= len(self.nodes):
            return 1
        return 2

    def __str__(self):
        final_str = ""
        for each_node in self.nodes:
            final_str += str(each_node)
        return final_str


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

    def __str__(self):
        return str(self.value)

if __name__ == '__main__':
    my_heap = Heap()
    my_heap.insert(("07", 7))
    my_heap.insert(("05", 5))
    my_heap.insert(("01", 1))
    my_heap.insert(("03", 3))
    my_heap.insert(("02", 2))
    my_heap.insert(("04", 4))
    my_heap.insert(("06", 6))
    my_heap.delete_max()
    print(str(my_heap))
    # print(my_heap.root_node.left_child.value)
    # print(my_heap.root_node.right_child.value)
    # print(my_heap.root_node.right_child.left_child.value)
    # print(my_heap.root_node.left_child.right_child.value)
    # print("")
    # print(my_heap)
