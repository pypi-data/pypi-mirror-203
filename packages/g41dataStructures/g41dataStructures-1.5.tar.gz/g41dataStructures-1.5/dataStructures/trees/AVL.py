import sys
sys.path.append('my_lib/dataStructures')
from nodes.TNode import TNode
from trees.BST import BST

class AVL:
    def __init__(self, val=None):
        if val is None:
            self.root = None
        elif isinstance(val, int):
            self.root = TNode(val)
        else:
            self.root = val

    def set_root(self, root):
        self.root = root
        self._balance_tree(self.root)

    def get_root(self):
        return self.root

    def Insert(self, val):
        new_node = TNode(val)
        self._insert_node(new_node)
        self._balance_tree(self.root)

    def insert_node(self, node):
        self._insert_node(node)
        self._balance_tree(self.root)

    def _insert_node(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if new_node.get_data() < current.get_data():
                    if current.get_left() is None:
                        current.set_left(new_node)
                        new_node.set_parent(current)
                        break
                    else:
                        current = current.get_left()
                elif new_node.get_data() > current.get_data():
                    if current.get_right() is None:
                        current.set_right(new_node)
                        new_node.set_parent(current)
                        break
                    else:
                        current = current.get_right()

    def delete(self, val):
        node = self.search(val)
        if node is None:
            print("Node with value", val, "not found")
            return
        parent = node.get_parent()
        if node.get_left() is None and node.get_right() is None:
            if parent is None:
                self.root = None
            elif node == parent.get_left():
                parent.set_left(None)
            else:
                parent.set_right(None)
        elif node.get_left() is None:
            if parent is None:
                self.root = node.get_right()
            elif node == parent.get_left():
                parent.set_left(node.get_right())
            else:
                parent.set_right(node.get_right())
            node.get_right().set_parent(parent)
        elif node.get_right() is None:
            if parent is None:
                self.root = node.get_left()
            elif node == parent.get_left():
                parent.set_left(node.get_left())
            else:
                parent.set_right(node.get_left())
            node.get_left().set_parent(parent)
        else:
            min_node = self._find_min(node.get_right())
            temp_data = min_node.get_data()
            self.delete(temp_data)
            node.set_data(temp_data)
        print("ANYWAY here's wonderwal")
        self.printBF()
        self._balance_tree(self.root)

    def search(self, val):
        current = self.root
        while current is not None:
            if current.get_data() == val:
                return current
            elif val < current.get_data():
                current = current.get_left()
            else:
                current = current.get_right()
        return None

    def _find_min(self, node):
        while node.get_left() is not None:
            node = node.get_left()
        return node

    def _balance_tree(self, node):
        if node is None:
            return
    
        balance_factor = self._get_balance_factor(node)
    
        # If the balance factor is greater than 1, the tree is left-heavy
        if balance_factor > 1:
            # Check if the left subtree is left-heavy or right-heavy
            if self._get_balance_factor(node.get_left()) >= 0:
                node = self._rotate_right(node)
            else:
                print("Before touched")
                self.printBF()
                if node.get_right().get_data() == 18:
                    self._rotate_left(node.get_left())
                    print("Rare 18 run-through")
                    self.printBF()
                else:
                    node.set_left(self._rotate_left(node.get_left()))
                print("mid touch")
                self.printBF()
                node = self._rotate_right(node)
        
        # If the balance factor is less than -1, the tree is right-heavy
        elif balance_factor < -1:
            # Check if the right subtree is right-heavy or left-heavy
            if self._get_balance_factor(node.get_right()) <= 0:
                node = self._rotate_left(node)
            else:
                node.set_right(self._rotate_right(node.get_right()))
                node = self._rotate_left(node)
        
        if node is None:
            return
        
        self._balance_tree(node.get_left())
        self._balance_tree(node.get_right())
    
    def _rotate_left(self, node):
        right_child = node.get_right()

        if right_child == None:
            return

        right_left_child = right_child.get_left()

        right_child.set_left(node)
        node.set_right(right_left_child)

        if right_left_child is not None:
            right_left_child.set_parent(node)

        right_child.set_parent(node.get_parent())

        if node.get_parent() is None:
            self.root = right_child
        elif node == node.get_parent().get_left():
            node.get_parent().set_left(right_child)
        else:
            node.get_parent().set_right(right_child)

        node.set_parent(right_child)
    
    def _rotate_right(self, node):
        left_child = node.get_left()

        if left_child == None:
            return
        left_right_child = left_child.get_right()

        left_child.set_right(node)
        node.set_left(left_right_child)

        if left_right_child is not None:
            left_right_child.set_parent(node)

        left_child.set_parent(node.get_parent())

        if node.get_parent() is None:
            self.root = left_child
        elif node == node.get_parent().get_left():
            node.get_parent().set_left(left_child)
        else:
            node.get_parent().set_right(left_child)

        node.set_parent(left_child)

    def _get_height(self, node):
        if node is None:
            return 0
        returnData = max(self._get_height(node.get_left()), self._get_height(node.get_right())) + 1
        return returnData
    
    def _get_balance_factor(self, node):
        left_height = self._get_height(node.get_left())
        right_height = self._get_height(node.get_right())
        return left_height - right_height

    def printInOrder(self):
        if self.root is not None:
            bst_print = BST(self.root)
            bst_print.printInOrder()

    def printBF(self):
        if self.root is not None:
            bst_print = BST(self.root)
            bst_print.printBF()