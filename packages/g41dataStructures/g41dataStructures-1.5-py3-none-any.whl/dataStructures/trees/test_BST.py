import sys
sys.path.append('my_lib/dataStructures')
from trees.BST import BST
from nodes.TNode import TNode

def test_BST_constructor_none():
    bst = BST()

    assert bst.get_root() == None

def test_BST_constructor_data():
    bst = BST(5)

    assert bst.get_root().get_data() == 5

def test_BST_constructor_TNode():
    test_node = TNode(24)
    bst = BST(test_node)

    assert bst.get_root().get_data() == 24

def test_set_root_int():
    bst = BST(212)

    bst.set_root(5)

    assert bst.get_root().get_data() == 5

def test_set_root_TNode():
    bst = BST(41)

    test_node = TNode(87)

    bst.set_root(test_node)

    assert bst.get_root().get_data() == 87

def test_insert_int():
    bst = BST(10)

    bst.insert(15)

    assert bst.get_root().get_right().get_data() == 15

def test_insert_TNode():
    bst = BST(255)

    test_node = TNode(1)

    bst.insert(test_node)

    assert bst.get_root().get_left().get_data() == 1

def test_delete_leaf():
    bst = BST(8)

    bst.insert(4)

    bst.insert(14)
    bst.insert(19)

    bst.delete(4)

    assert bst.get_root().get_left() == None

def test_delete_nonleaf():
    bst = BST(8)

    bst.insert(4)
    bst.insert(7)

    bst.insert(14)
    bst.insert(19)

    bst.delete(4)

    assert bst.get_root().get_left().get_data() == 7

def test_search():
    bst = BST(15)

    bst.insert(7)
    bst.insert(5)
    bst.insert(23)
    bst.insert(3)
    bst.insert(17)

    actualNode = bst.search(23)
    expectedNode = TNode(23).get_data()

    assert actualNode.get_data() == expectedNode

def test_wrong_search():
    bst = BST(15)

    bst.insert(7)
    bst.insert(5)
    bst.insert(23)
    bst.insert(3)
    bst.insert(17)

    actualNode = bst.search(13)

    assert actualNode == None