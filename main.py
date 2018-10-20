from entity import SimpleTree as st
from utils import find as f

tree = st.SimpleTree()

tree.add_node(None, 5)
tree.add_node(5, 7)
tree.add_node(5, 25)
tree.add_node(5, 125)
tree.add_node(7, 40)
tree.add_node(7, 45)
tree.add_node(125, 145)
tree.add_node(40, 100500)
tree.add_node(100500, 1)


# print(tree)
# print(tree.root)
# print(tree.root.children)
#
# print(tree.root.value)
#
# for child in tree.root.children:
#     print('Child: ' + str(child.value))
#     print('parent: ' + str(child.parent.value))
#     print()
#     if len(child.children) > 0:
#         print('У узла ' + str(child.value) + ' есть потомки')
#         print('^^^^^^^^^^^^^^^^^^')
#         for ch in child.children:
#             print('papa: ' + str(ch.parent.value))
#             print(ch.value)
#         print('^^^^^^^^^^^^^^^^^^')

print(tree.get_values_list())

# h = f.find(tree.root, 100500)
# print(h)
# print(h.value)
# print(h.parent.value)
# print(h.children)

tree.remove_node(7)

print(tree.get_values_list())