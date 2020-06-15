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



