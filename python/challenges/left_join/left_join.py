from hashtable import HashTable
from linkedlist import LinkedList


def left_join_tables(hashtable1, hashtable2):
    """[summary]
    This function takes in 2 hashtables and returns an array after
    combining both data structures using left join method.
    
    """
    hashtable3 = HashTable(11)
    ht1_keys = []
    ht3_data = []

    for item in hashtable1._buckets:
        if item:
            ht1_keys.append(item.get_keys())
    
    for bucket in ht1_keys:
        for key in bucket:
            value1 = hashtable1.get(key)
            value2 = None
            if hashtable2.contains(key):
                value2 = hashtable2.get(key)
                hashtable3.add(key, value1, value2)
            else:
                hashtable3.add(key, value1)
            
            ht3_data.append((key, value1, value2))
    
    for item in hashtable3._buckets:
        if item:
            item.display()
    
    return ht3_data


hashtable = HashTable(11)
hashtable.add('Chuck', 'one')
hashtable.add('Laura', 'two')
hashtable.add('Alex', 'three')
hashtable.add('Ben', 'four')
hashtable.add('Maddie', 'five')

hashtable2 = HashTable(11)
hashtable2.add('Ben', '4')
hashtable2.add('Alex', '3')
hashtable2.add('Mary', '6')
hashtable2.add('Alfred', '7')
hashtable2.add('Laura', '2')
hashtable2.add('Chuck','1')


data = left_join_tables(hashtable, hashtable2)
