from myLib.datastructures.nodes.TNode import TNode
from myLib.datastructures.trees.BST import BST
from queue import Queue

class AVL(BST):
    def __init__(self, root=None):
        super().__init__(root)

   
    def set_root(self, root):
        super().set_root(root)
        if self.root.get_left() is not None or self.root.get_right() is not None:
            self.balance_tree()

    def get_root(self):
        return self.root

    def insert(self, val):
        super().insert(val)
        self.balance_tree()

    def insert_node(self, node):
        super().insert_node(node)
        self.balance_tree()

    def balance_tree(self):
        if self.root is None:
            return
        if self.root.get_left() is not None:
            self.balance_tree_helper(self.root.get_left())
        if self.root.get_right() is not None:
            self.balance_tree_helper(self.root.get_right())
        self.update_balance(self.root)
        self.rotate_tree(self.root)

    def balance_tree_helper(self, node):
        if node is None:
            return
        if node.get_left() is not None:
            self.balance_tree_helper(node.get_left())
        if node.get_right() is not None:
            self.balance_tree_helper(node.get_right())
        self.update_balance(node)
        self.rotate_tree(node)

    def update_balance(self, node):
        left_height = self.get_height(node.get_left())
        right_height = self.get_height(node.get_right())
        balance = left_height - right_height
        node.set_balance(balance)

    def rotate_tree(self, node):
        if node.get_balance() > 1:
            if node.get_left().get_balance() < 0:
                self.rotate_left(node.get_left())
            self.rotate_right(node)
        elif node.get_balance() < -1:
            if node.get_right().get_balance() > 0:
                self.rotate_right(node.get_right())
            self.rotate_left(node)

    def rotate_left(self, node):
        right = node.get_right()
        parent = node.get_parent()
        if parent is None:
            self.root = right
            right.set_parent(None)
        elif node == parent.get_left():
            parent.set_left(right)
            right.set_parent(parent)
        else:
            parent.set_right(right)
            right.set_parent(parent)
        node.set_right(right.get_left())
        if right.get_left() is not None:
            right.get_left().set_parent(node)
        right.set_left(node)
        node.set_parent(right)
        self.update_balance(node)
        self.update_balance(right)

    def rotate_right(self, node):
        left = node.get_left()
        parent = node.get_parent()
        if parent is None:
            self.root = left
            left.set_parent(None)
        elif node == parent.get_left():
            parent.set_left(left)
            left.set_parent(parent)
        else:
            parent.set_right(left)
            left.set_parent(parent)
        node.set_left(left.get_right())
        if left.get_right() is not None:
            left.get_right().set_parent(node)
        left.set_right(node)
        node.set_parent(left)
        self.update_balance(node)
        self.update_balance(left)

    def get_height(self, node):
        if node is None:
            return -1
        return 1 + max(self.get_height(node.get_left()), self.get_height(node.get_right()))
    
    def delete(self, val):
        super().delete(val)

