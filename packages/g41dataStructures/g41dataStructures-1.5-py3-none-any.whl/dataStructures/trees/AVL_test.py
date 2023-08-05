import sys
sys.path.append('my_lib/dataStructures')
from trees.AVL import AVL

def main():
    # create an empty AVL tree
    avl = AVL()

    # insert some values
    avl.insert(5)
    avl.insert(3)
    avl.insert(7)
    avl.insert(2)
    avl.insert(4)
    avl.insert(6)
    avl.insert(8)

    # print the tree in order traversal
    print("In-order traversal:")
    avl.printInOrder()

    # print the tree breadth-first traversal
    print("Breadth-first traversal:")
    avl.printBF()

    # delete a value and print the tree again
    avl.delete(5)
    print("In-order traversal after deleting 5:")
    avl.printInOrder()
    avl.printBF()

    avl.delete(3)
    avl.delete(4)

    avl.printInOrder()
    avl.printBF()

    avl.delete(6)
    avl.delete(7)

    avl.printInOrder()
    avl.printBF()

if __name__ == '__main__':
    main()
