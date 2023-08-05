import sys
sys.path.append('my_lib/dataStructures')
from nodes.TNode import TNode
from BST import BST

def main():
    # Create a binary search tree with root node 8
    bst = BST(8)

    # Insert nodes with values 3, 10, 1, 6, 14, 4, and 7
    bst.insert(3)
    bst.insert(10)
    bst.insert(1)
    bst.insert(6)
    bst.insert(14)
    bst.insert(4)
    bst.insert(7)

    # Print the binary search tree in order
    bst.printInOrder()

    # Print the binary search tree in breadth-first order
    bst.printBF()

    # Delete the node with value 6 from the binary search tree
    bst.delete(6)

    # Print the binary search tree in order after deleting the node with value 6
    bst.printInOrder()

if __name__ == '__main__':
    main()
