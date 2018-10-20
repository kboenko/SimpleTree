def find(tree, elem):
    if tree.value == elem:
        return tree
    elif len(tree.children) > 0:
        for child in tree.children:
            subtree = find(child, elem)
            return subtree
    else:
        return None