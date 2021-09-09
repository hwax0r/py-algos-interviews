class Node:
    def __init__(self, obj, children=None):
        self.obj = obj
        if children is not None:
            self.children = children
        else:
            self.children = []


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
#         a
#   b            c
# d   e        f    g
a.children = [b, c]
b.children = [d, e]
c.children = [f, g]


class node_bin:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


aa = node_bin(100)
bb = node_bin(50)
cc = node_bin(150)
dd = node_bin(25)
ee = node_bin(75)
ff = node_bin(125)
gg = node_bin(175)
hh = node_bin(12)
ii = node_bin(9)
jj = node_bin(10)

#                     aa
#           bb                    cc
#     dd          ee          ff         gg
#   hh   *      *   ii      *   *     jj   *

#                     100
#           50                    150
#     25          75          125         175
#   12  *        *   90      *   *      169   *


aa.left, aa.right = bb, cc
bb.left, bb.right = dd, ee
dd.left, dd.right = hh, None
ee.left, ee.right = None, ii
cc.left, cc.right = ff, gg
ff.left, ff.right = None, None
gg.left, gg.right = jj, None


def direct_traversal(vertex: Node) -> None:
    print(vertex.obj)
    for child in vertex.children:
        direct_traversal(child)


def reverse_traversal(vertex: Node) -> None:
    for child in vertex.children:
        reverse_traversal(child)
    print(vertex.obj)


def lmr_traversal(vertex) -> None:
    # only for binary tree
    # left - middle - right
    if vertex.left is not None:
        lmr_traversal(vertex.left)
    print(vertex.value)
    if vertex.right is not None:
        lmr_traversal(vertex.right)


def insert_node(root: node_bin, key: int) -> None:
    # only for bin tree
    if root.value > key:
        if root.left is None:
            root.left = node_bin(key)
        else:
            insert_node(root.left, key)
    elif root.value <= key:
        if root.right is None:
            root.right = node_bin(key)
        else:
            insert_node(root.right, key)
