class Node:

    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

    # def set_head(self, input_head):
    #     self.head = input_head
    #     if self.next_node is not None:
    #         self.next_node.set_head(input_head)

    def add_node(self, new_node):
        if self.next_node is None:
            self.next_node = new_node
        else:
            temp = self.next_node
            self.next_node = new_node
            new_node.add_node(temp)


class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, head_node):
        self.head = head_node

    def append(self, new_node):
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            if self.tail.next_node is not None:
                self.update_tail()
            self.tail.add_node(new_node)
            self.tail = new_node

    def unshift(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            new_node.add_node(temp)

    def update_tail(self):
        current_node = self.tail
        while (current_node.next_node is not None):
            current_node = current_node.next_node
        self.tail = current_node


def print_node(node):
    print("value: " + str(node.value))

if __name__ == '__main__':
    my_node1 = Node(1, None)
    my_node3 = Node(3, None)
    my_node2 = Node(2, None)
    my_node4 = Node(4, None)
    my_ll1 = Linked_List()
    my_ll1.append(my_node2)
    my_node2.add_node(my_node3)
    my_ll1.unshift(my_node1)
    my_node1.add_node(my_node4)
    print_node(my_node1)
    print_node(my_node1.next_node)
    print_node(my_node1.next_node.next_node)
    print_node(my_node1.next_node.next_node.next_node)
