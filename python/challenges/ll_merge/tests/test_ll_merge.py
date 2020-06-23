from ll_merge import __version__
from ll_merge.ll_merge import MergeLists

def test_version():
    assert __version__ == '0.1.0'


def test_merge_exists():
    assert MergeLists


def test_merge_lists():
    ll1 = Linkedlist()
    ll2 = Linkedlist()
    ll1.insert(3)
    ll1.insert(2)
    ll1.insert(1)
    ll2.insert(6)
    ll2.insert(5)
    ll2.insert(4)
    merged_lists = Linkedlist.merge_lists(ll1, ll2)
    assert merged_lists.head = 1
    assert merged_lists.next_node = 4