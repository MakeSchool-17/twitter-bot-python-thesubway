from linked_list import *


class Stack:

    def __init__(self):
        self.head = None
        self.size = 0
        pass

    def push(self, value):
        new_node = Node(value)
        next_node = self.head
        if self.head:
            self.head = new_node
            self.head.next_node = next_node
        else:
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            first_element = self.head
            self.head = first_element.next_node
            self.size -= 1
            return first_element.value

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.value

    def size(self):
        return self.size

    # overrides the to_str method
    def __str__(self):
        return_str = ''
        current_node = self.head
        while current_node is not None:
            return_str = return_str + str(current_node.value) + ' '
            current_node = current_node.next_node
        return return_str

    def is_empty(self):
        return self.head is None


if __name__ == '__main__':
    test_stack = Stack()
    test_stack.push('a')
    test_stack.push('b')
    test_stack.push('c')
    print(str(test_stack))
    first_item = test_stack.pop()
    print('popped' + str(first_item))
