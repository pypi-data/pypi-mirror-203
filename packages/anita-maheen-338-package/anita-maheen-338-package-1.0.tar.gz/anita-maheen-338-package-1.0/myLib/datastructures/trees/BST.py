from myLib.datastructures.nodes.TNode import TNode

from queue import Queue

class BST:
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def insert(self, val):
        node = TNode(val)
        if self.root is None:
            self.root = node
            return
        curr = self.root
        while True:
            if val < curr.get_data():
                if curr.get_left() is None:
                    curr.set_left(node)
                    node.set_parent(curr)
                    return
                curr = curr.get_left()
            else:
                if curr.get_right() is None:
                    curr.set_right(node)
                    node.set_parent(curr)
                    return
                curr = curr.get_right()

    def insert_node(self, node):
        if self.root is None:
            self.root = node
            return

        curr_node = self.root

        while True:
            if node.get_data() < curr_node.get_data():
                if curr_node.get_left() is None:
                    curr_node.set_left(node)
                    node.set_parent(curr_node)
                    break
                curr_node = curr_node.get_left()
            else:
                if curr_node.get_right() is None:
                    curr_node.set_right(node)
                    node.set_parent(curr_node)
                    break
                curr_node = curr_node.get_right()

    def delete(self, val):
        if self.root is None:
            print("Value not found in the tree")
            return
        node = self.search(val)
        if node is None:
            print("Value not found in the tree")
            return
        parent = node.get_parent()
        if node.get_left() is None and node.get_right() is None:
            if parent is None:
                self.root = None
            elif node == parent.get_left():
                parent.set_left(None)
            else:
                parent.set_right(None)
            result = self._print_in_order_helper(self.root, [])
            if node.get_data() in result:
                result.remove(node.get_data())
            del node
        elif node.get_left() is None or node.get_right() is None:
            child = node.get_left() or node.get_right()
            child.set_parent(parent)  # update child's parent pointer
            if parent is None:
                self.root = child
            elif node == parent.get_left():
                parent.set_left(child)
            else:
                parent.set_right(child)
            result = self._print_in_order_helper(self.root, [])
            if node.get_data() in result:
                result.remove(node.get_data())
            del node
        else:
            succ = self.get_successor(node)
            node.set_data(succ.get_data())
            curr = succ.get_right()
            parent = succ.get_parent()
            if curr is not None:
                curr.set_parent(parent)
            if parent.get_left() == succ:
                parent.set_left(curr)
            else:
                parent.set_right(curr)
            result = self._print_in_order_helper(self.root, [])
            if node.get_data() in result:
                result.remove(node.get_data())
            del succ

    def search(self, val):
        curr = self.root
        while curr is not None:
            if curr.get_data() == val:
                return curr
            elif val < curr.get_data():
                curr = curr.get_left()
            else:
                curr = curr.get_right()
        return None


    def print_in_order(self):
        if self.root is None:
            return
        result = []
        self._print_in_order_helper(self.root, result)
        print(" ".join(str(x) for x in sorted(result)))

    def _print_in_order_helper(self, node, result):
        if node is None:
            return result
        result = self._print_in_order_helper(node.get_left(), result)
        if node.get_data() is not None:
            result.append(node.get_data())
        result = self._print_in_order_helper(node.get_right(), result)
        return result


    def print_bf(self):
        if self.root is None:
            return
        q = Queue()
        q.put(self.root)
        while not q.empty():
            level_size = q.qsize()
            level_nodes = []
            for i in range(level_size):
                node = q.get()
                level_nodes.append(node.get_data())
                if node.get_left() is not None:
                    q.put(node.get_left())
                if node.get_right() is not None:
                    q.put(node.get_right())
            print(*level_nodes, end=" ")
            print()

    def get_successor(self, node):
        curr = node.get_right()
        while curr.get_left() is not None:
            curr = curr.get_left()
        return curr


