from hashtable import HashTable
from left_join import left_join_tables
from linkedlist import LinkedList


ht1 = HashTable(11)
ht1.add('fond', 'enamored')
ht1.add('wrath', 'anger')
ht1.add('diligent', 'employed')
ht1.add('outfit', 'garb')
ht1.add('guide', 'usher')

ht2 = HashTable(11)
ht2.add('fond', 'averse')
ht2.add('wrath', 'delight')
ht2.add('diligent', 'idle')
ht2.add('guide', 'follow')
ht2.add('flow', 'jam')


def test_hashtable_exists():
    HashTable


def test_linkedlist_exists():
    LinkedList


def test_left_join_exists():
    left_join_tables


def test_left_join_with_2_values():
    data = left_join_tables(ht1, ht2)
    acutal = data[0]
    expected = ('wrath', 'anger', 'delight')
    assert acutal == expected


def test_left_join_with_1_value():
    data = left_join_tables(ht1, ht2)
    acutal = data[3]
    expected = ('outfit', 'garb', None)
    assert acutal == expected