from hashtable import HashTable


# Adding a key/value to your hashtable results in the value being in the data structure
# Retrieving based on a key returns the value stored
# Successfully returns null for a key that does not exist in the hashtable
# Successfully handle a collision within the hashtable
# Successfully retrieve a value from a bucket within the hashtable that has a collision
# Successfully hash a key to an in-range value

def test_hashtable_default_size():
    hashtable = HashTable()
    actual = hashtable.size
    expected = 1024
    assert actual == expected


def test_hashtable_custom_size():
    hashtable = HashTable(30)
    actual = hashtable.size
    expected = 30
    assert actual == expected


def test_hashtable_custom_size_fail():
    hashtable = HashTable(30)
    actual = hashtable.size
    expected = 35
    assert actual != expected


def test_single_hash_pass():
    hashtable = HashTable()
    hashtable.add('Chuck', 45)
    actual = hashtable.get('Chuck')
    expected = 45
    assert actual == expected


def test_single_hash_fail():
    hashtable = HashTable()
    hashtable.add('Chuck', 40)
    actual = hashtable.get('Chuck')
    expected = 45
    assert actual != expected


def test_contains_pass_true():
    hashtable = HashTable()
    hashtable.add('Chuck', 40)
    expected = hashtable.contains('Chuck')
    actual = True
    assert actual == expected


def test_contains_pass_false():
    hashtable = HashTable()
    hashtable.add('Chuck', 40)
    expected = hashtable.contains('Daniel')
    actual = False
    assert actual == expected


def test_contains_pass_with_collsion():
    hashtable = HashTable()
    hashtable.add('Chuck', 40)
    hashtable.add('kcuhC', 33)
    hashtable.add('Ckcuh', 11)
    expected = hashtable.contains('kcuhC')
    actual = True
    assert actual == expected


def test_contains_fail():
    hashtable = HashTable()
    hashtable.add('Chuck', 40)
    expected = hashtable.contains('Daniel')
    actual = True
    assert actual != expected


def test_add_multiple_hash_pass():
    hashtable = HashTable()
    hashtable.add('Chuck', 45)
    hashtable.add('kcuhC', 33)
    hashtable.add('Ckcuh', 11)
    actual = hashtable.get('Ckcuh')
    expected = 11
    assert actual == expected
