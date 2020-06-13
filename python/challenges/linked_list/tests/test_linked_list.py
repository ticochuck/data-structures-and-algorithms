from linked_list import __version__
from linked_list.linked_list import Node, LinkedList

def test_version():
    assert __version__ == '0.1.0'


# Write tests to prove the following functionality:

# Can successfully instantiate an empty linked list
# Can properly insert into the linked list
# The head property will properly point to the first node in the linked list
# Can properly insert multiple nodes into the linked list
# Will return true when finding a value within the linked list that exists
# Will return false when searching for a value in the linked list that does not exist
# Can properly return a collection of all the values that exist in the linked list

def test_node_exist():
    assert Node


def test_LinkedList_exist():
    assert LinkedList

