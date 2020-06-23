from ll_merge import __version__
from ll_merge.ll_merge import LinkedList, Node

def test_version():
    assert __version__ == '0.1.0'


def test_merge_exists():
    assert LinkedList.merge_lists


def test_list():
    ll = LinkedList()
    assert ll

def test_lists():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.insert(3)
    ll1.insert(2)
    ll1.insert(1)
    ll2.insert(6)
    ll2.insert(5)
    ll2.insert(4)
    assert ll1.head.value == 1
    assert ll2.head.value == 4    


def test_merge_lists():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.insert(1)
    ll1.insert(1)
    ll1.insert(1)
    ll2.insert(2)
    ll2.insert(2)
    ll2.insert(2)
    merged = LinkedList.merge_lists(ll1, ll2)
    assert merged.value == 1
    assert merged.next_node.value == 2
    assert merged.next_node.next_node.value == 1





