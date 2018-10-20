from utils import find as f
from utils import get_values as g
from entity import Node as n

class SimpleTree:

    def __init__(self):
        self.root = None

    def add_node(self, elem_value, value):
        if self.root == None:
            self.root = n.Node(value)
            return
        elif self.root.value == elem_value:
            node = n.Node(value)
            node.set_parent(self.root)
            self.root.children.append(node)
        elif self.root.value != elem_value and len(self.root.children) > 0:
            for child in self.root.children:
                subtree = f.find(child, elem_value)
                if subtree is not None:
                    ch_node = n.Node(value)
                    ch_node.set_parent(subtree)
                    subtree.children.append(ch_node)
                    return

    def remove_node(self, value):
        if len(self.root.children) > 0:
            for element in self.root.children:
                item = f.find(element, value)
                if item is not None:
                    if len(item.children) == 0:
                        item.parent.children.remove(item)
                    else:
                        for child in item.children:
                            child.set_parent(item.parent)
                            item.parent.children.append(child)
                        item.parent.children.remove(item)

    def get_values_list(self):
        result = []
        if self.root is not None:
            result.append(self.root.value)
            if len(self.root.children) > 0:
                for child in self.root.children:
                    result.append(child.value)
                    g.get_values(child, result)
        return result

    def find_values(self, value):
        pass

    def move_node(self, value, new_parent):
        pass

    def get_tree_info(self):
        pass

    def get_depths(self):
        pass