import sys
sys.path.append('my_lib/dataStructures')
from nodes.TNode import TNode

def test_empty_constructor():
    tnode = TNode()
    successData = False
    successParent = False
    successChildren = False

    if tnode.get_data() == 0 and tnode.get_balance() == 0:
        successData = True

    if tnode.get_left() == None and tnode.get_right() == None:
        successChildren = True

    if tnode.get_parent() == None:
        successParent = True

    assert (successParent and successChildren and successData) == True

def test_full_constructor():
    tnodeParent = TNode(9)
    tnodeLeft = TNode(3)
    tnodeRight = TNode(7)
    tnode = TNode(5, 1, tnodeParent, tnodeLeft, tnodeRight)
    success = True

    if(tnode.get_data() != 5 or tnode.get_balance() != 1 or tnode.get_parent().get_data() != 9):
        success = False

    if(tnode.get_left().get_data() != 3 or tnode.get_right().get_data() != 7):
        success = False

    assert success == True

def test_set_datas():
    tnode = TNode(8, 2)

    tnode.set_data(3)
    tnode.set_balance(0)

    assert tnode.get_data() == 3 and tnode.get_balance() == 0

def test_set_nodes():
    tnode = TNode(150)
    tnodeP = TNode(200)
    tnodeL = TNode(75)
    tnodeR = TNode(175)
    success = True

    tnode.set_parent(tnodeP)
    tnode.set_left(tnodeL)
    tnode.set_right(tnodeR)

    if(tnode.get_parent().get_data() != 200 or tnode.get_left().get_data() != 75  or tnode.get_right().get_data() != 175):
        success = False

    assert success == True

def test_string_toData():
    tnode = TNode(18, -1, TNode(40), TNode(7), None)
    expectedString = "18"

    assert expectedString == tnode.__str__()