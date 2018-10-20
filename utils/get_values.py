def get_values(tree, res):
    if len(tree.children) > 0:
        for child in tree.children:
            res.append(child.value)
            get_values(child, res)