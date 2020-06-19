from linked_list import __version__
from linked_list.linked_list import Node, LinkedList

def test_version():
    assert __version__ == '0.1.0'


def test_node_exist():
    assert Node


def test_LinkedList_exist():
    assert LinkedList

def test_empty_list():
    ll = LinkedList()
    assert ll

def test_insert_to_empty_list():
    ll = LinkedList()
    ll.insert('Sunday')
    assert ll.head.value == 'Sunday'

def test_insert_multiple_to_empty_list():
    ll = LinkedList()
    ll.insert('Tuesday')
    ll.insert('Monday')
    ll.insert('Sunday')
    assert ll.head.value == 'Sunday'

def test_next_node_value():
    ll = LinkedList()
    ll.insert('Tuesday')
    ll.insert('Monday')
    ll.insert('Sunday')
    assert ll.head.next_node.value == 'Monday'

def test_includes_value_true():
    ll = LinkedList()
    ll.includes('Monday')
    assert True

def test_includes_value_false():
    ll = LinkedList()
    actual = ll.includes('November')
    expected = False
    assert actual == expected

def test_append():
    ll3 = LinkedList()
    ll3.insert(4)
    ll3.insert(3)
    ll3.insert(2)
    ll3.insert(1)
    ll3.append(5)
    actual = str(ll3)
    expected = "head: 1, Next_Node=2, Next_Node=3, Next_Node=4, Next_Node=5, Next_Node=None"
    

def test_insert_before_strings():
    ll2 = LinkedList()
    ll2.insert('Bye')
    ll2.insert('Hola')
    ll2.insert('Hi')
    ll2.insert_before('Hola', 'Adios')
    actual = str(ll2)
    expected = "head: Hi, Next_Node=Adios, Next_Node=Hola, Next_Node=Bye, Next_Node=None"
    assert actual == expected

def test_insert_before_head():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(3)
    ll.insert(1)
    ll.insert_before(1, 5)
    actual = str(ll)
    expected = "head: 5, Next_Node=1, Next_Node=3, Next_Node=2, Next_Node=None"
    assert actual == expected


def test_insert_before():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(3)
    ll.insert(1)
    ll.insert_before(3, 5)
    actual = str(ll)
    expected = "head: 1, Next_Node=5, Next_Node=3, Next_Node=2, Next_Node=None"
    assert actual == expected
    
    
def test_insert_before_exception():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(3)
    ll.insert(1)
    actual = ll.insert_before(4, 5)
    expected = 'Node with value of 4 does not exist'
    assert actual == expected


def test_insert_after():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(3)
    ll.insert(1)
    ll.insert_after(3, 5)
    actual = str(ll)
    expected = "head: 1, Next_Node=3, Next_Node=5, Next_Node=2, Next_Node=None"
    assert actual == expected


def test_insert_after():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(3)
    ll.insert(1)
    ll.insert_after(2, 5)
    actual = str(ll)
    expected = "head: 1, Next_Node=3, Next_Node=2, Next_Node=5, Next_Node=None"
    assert actual == expected

def test_insert_after_exception():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(3)
    ll.insert(1)
    actual = ll.insert_before(6, 5)
    expected = 'Node with value of 6 does not exist'
    assert actual == expected

def test_kth_value():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_value(2)
    expected = 3
    assert actual == expected


def test_kth_value_with_0():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_value(0)
    expected = 2
    assert actual == expected

def test_kth_value_exception():
    ll = LinkedList()
    ll.insert(2)
    ll.insert(8)
    ll.insert(3)
    ll.insert(1)
    actual = ll.kth_value(6)
    expected = "Exception"
    assert actual == expected