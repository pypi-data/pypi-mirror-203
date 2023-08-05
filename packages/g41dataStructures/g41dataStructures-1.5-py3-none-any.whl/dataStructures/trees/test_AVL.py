import sys
sys.path.append('my_lib/dataStructures')
from trees.AVL import AVL
from nodes.TNode import TNode

def test_init():
    avl = AVL()

    assert avl.get_root() == None

def test_constructor_integer():
    avl = AVL(5)
    success = False

    if avl.get_root().get_data() == 5:
        success = True

    assert success == True

def test_constructor_TNode():
    test_node = TNode(12)
    avl = AVL(test_node)


    assert avl.get_root().get_data() == 12

def test_Insert():
    avl = AVL()

    avl.Insert(5)

    assert avl.get_root().get_data() == 5

def test_Insert_multiple():
    avl = AVL()
    success = False

    avl.Insert(3)
    avl.Insert(7)
    avl.Insert(2)
    avl.Insert(4)

    if(avl.get_root().get_data() == 3 and avl.get_root().get_left().get_data() == 2 and avl.get_root().get_right().get_data() == 7):
        success = True

    assert success == True

def test_delete_leaf_node():
    avl = AVL(10)

    avl.Insert(5)
    avl.delete(5)

    assert avl.get_root().get_left() == None

def test_delete_root():
    avl = AVL(4)


    avl.Insert(2)
    avl.Insert(8)
    avl.Insert(7)

    avl.delete(4)

    assert avl.get_root().get_data() == 7

def test_balancing_uneven():
    test_node = TNode(10)
    success = False
    avl = AVL(test_node)

    avl.Insert(3)
    avl.Insert(14)

    avl.Insert(1)

    avl.printBF()
    avl.printInOrder()

    if(avl.get_root().get_data() == 10):
        success = True

    assert success == True

def test_Insert_No_Pivot():
    avl = AVL(15)

    avl.Insert(5)
    avl.Insert(25)

    avl.Insert(30)

    right_root = avl.get_root().get_right()

    assert right_root.get_right().get_data() == 30



def test_Insert_Pivot_Exists():
    avl = AVL(31)

    avl.Insert(20)

    avl.Insert(40)
    avl.Insert(45)

    avl.printBF()

    avl.Insert(15)

    left_child = avl.get_root().get_left()

    assert left_child.get_left().get_data() == 15

def test_Insert_outside():
    avl = AVL(10)

    avl.Insert(5)
    avl.Insert(15)

    avl.Insert(20)
    avl.Insert(25)
    avl.Insert(30)

    avl.Insert(35)
    avl.Insert(40)

    avl.Insert(3)
    avl.printBF()

    assert avl.get_root().get_data() == 25

def test_balancing_right_uneven():
    test_node = TNode(10)
    success = False
    avl = AVL(test_node)

    avl.Insert(24)
    avl.Insert(44)
    avl.Insert(18)

    avl.Insert(1)
    avl.Insert(2)
    avl.Insert(6)
    avl.Insert(5)

    avl.printBF()

    avl.delete(24)

    avl.printBF()
    avl.printInOrder()

    avl.delete(44)

    avl.printBF()

    if(avl.get_root().get_data() == 6):
        success = True

    assert success == True