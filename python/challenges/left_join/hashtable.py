from linkedlist import LinkedList


class HashTable:
    
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    
    def _hash(self, key):
        sum = 0
        for i in key:
            sum += ord(i)

        sum = sum * 199 # using a prime number but could be anything you want like ascii of first char

        return sum % self.size

        
    def add(self, key, value, value2=None):

        hashed_key = self._hash(key)

        if not self._buckets[hashed_key]:
           self._buckets[hashed_key] = LinkedList()
        
        self._buckets[hashed_key].append([key, value, value2])


    def get(self, key):
        hashed_key = self._hash(key)
        bucket = self._buckets[hashed_key]

        if bucket:
            current = bucket.head

            while current:
                if current.data[0] == key:
                    return current.data[1]
                current = current.next


    def contains(self, key):
        hashed_key = self._hash(key)

        if not self._buckets[hashed_key]:
            return False
        else:
            bucket = self._buckets[hashed_key]
            current = bucket.head

            while current:
                if current.data[0] == key:
                    return True
                current = current.next
   

    