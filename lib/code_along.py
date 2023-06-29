# regular tree
class Tree:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

#binary tree
class BinaryTree: # or binary search tree
    def __init__(self):
        self.root = None

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None