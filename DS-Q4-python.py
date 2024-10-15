class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top_node
        self.top_node = new_node

    def pop(self):
        if self.top_node is None:
            return None
        popped_data = self.top_node.data
        self.top_node = self.top_node.next
        return popped_data

    def top(self):
        if self.top_node is None:
            return None
        return self.top_node.data
    
