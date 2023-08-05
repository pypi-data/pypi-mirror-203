import sys
sys.path.append('my_lib/dataStructures')
from nodes.TNode import TNode

class BST:
    def __init__(self, val= None):
        if isinstance(val, int):
            self.root = TNode(val)
        elif isinstance(val, TNode):
            self.root = val
        else:
            self.root = None

    # Getter and setter for the root
    def get_root(self):
        return self.root

    def set_root(self, root):
        if isinstance(root, int):
            self.root = TNode(root)
        else:
            self.root = root

    # Insert a new node with the given value
    def insert(self, val):
        if isinstance(val, int):
            new_node = TNode(val)
            self.insert_node_recursive(self.root, new_node)
        else:
            self.insert_node_recursive(self.root, val)

    # Helper method for insert
    def insert_node_recursive(self, current_node, new_node):
        if new_node.data < current_node.data:
            if current_node.left is None:
                current_node.left = new_node
                new_node.parent = current_node
            else:
                self.insert_node_recursive(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
                new_node.parent = current_node
            else:
                self.insert_node_recursive(current_node.right, new_node)

    # Delete the node with the given value
    def delete(self, val):
        node_to_delete = self.search(val)
        if node_to_delete is None:
            print("Node not found")
            return
        if node_to_delete.left is None and node_to_delete.right is None:
            self.delete_leaf_node(node_to_delete)
        elif node_to_delete.left is None:
            self.delete_node_with_right_child(node_to_delete)
        elif node_to_delete.right is None:
            self.delete_node_with_left_child(node_to_delete)
        else:
            successor = self.get_successor(node_to_delete)
            node_to_delete.data = successor.data
            if successor.left is None and successor.right is None:
                self.delete_leaf_node(successor)
            else:
                self.delete_node_with_right_child(successor)

    # Deletes a leaf node from tree
    def delete_leaf_node(self, node):
        parent = node.parent
        if parent is None:
            self.root = None
        elif parent.left == node:
            parent.left = None
        else:
            parent.right = None

    # Deletes a node with a left child from tree
    def delete_node_with_left_child(self, node):
        parent = node.parent
        child = node.left
        child.parent = parent
        if parent is None:
            self.root = child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child

    # Delets a node with a right child from tree
    def delete_node_with_right_child(self, node):
        parent = node.parent
        child = node.right
        child.parent = parent
        if parent is None:
            self.root = child
        elif parent.left == node:
            parent.left = child
        else:
            parent.right = child

    # Helper method for delete
    def get_successor(self, node):
        successor = node.right
        while successor.left is not None:
            successor = successor.left
        return successor

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
    
    def printInOrder(self):
        self._printInOrder(self.root)
        print("\n")

    def _printInOrder(self, node):
        if node is not None:
            self._printInOrder(node.left)
            print(node.data, end=" ")
            self._printInOrder(node.right)

    def _get_depth(self, node):
        if node is None:
            return 0
        return 1 + max(self._get_depth(node.left), self._get_depth(node.right))

    def printBF(self):
        depth = self._get_depth(self.root)
        for i in range(1, depth+1):
            self._print_level(self.root, i)
            print()
        print()

    def _print_level(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.data, end=' ')
        else:
            self._print_level(node.left, level-1)
            self._print_level(node.right, level-1)