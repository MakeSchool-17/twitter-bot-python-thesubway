class Node:
    value = ""
    next_node = None
    head = None

    def __init__(self, value, next_node, head):
        self.value = value
        self.next_node = next_node
        self.head = head

    def add_node(new_node):
        next_node = new_node
        next_node.head = head


class Linked_List:
    temp = ""
    head = None
    tail = None

    def __init__(self, head):
        self.head = head


if __name__ == '__main__':
    my_node1 = Node(1, None, None)
    my_node2 = Node(2, None, my_node1)
    print(my_node1.value)
    print("2nd node's head: " + str(my_node2.head.value))
