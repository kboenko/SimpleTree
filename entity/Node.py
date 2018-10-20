class Node:

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    def set_parent(self, node):
        self.parent = node