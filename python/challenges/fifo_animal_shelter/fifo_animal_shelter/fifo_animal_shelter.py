class Node:
    """
    This is the Node class. 
    """
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_

class Queue:
    """
    Queue class that has a front property. 
    It creates an empty Queue when instantiated.
    """
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        Takes any value as an argument.
        Adds a new node with that value to the back of the queue
        """
        new_node = Node(value)
        if self.front:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = new_node
            self.rear = new_node

    
    def dequeue(self):
        """
        Removes the node from the front of the queue.
        Returns the node’s value.
        It raises an exception when called on empty queue.
        """
        if self.front:
            temp = self.front
            if self.front.next == None:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            temp.next = None
            return temp.value
        else:
            raise AttributeError('The queue is Empty')


class AnimalShelter:
    def __init__(self, name):
        """
        instantiates new shelter, cats and dogs queues
        """
        self.name = name
        self.cats = Queue()
        self.dogs = Queue()

    def enqueue(self, animal):
        """
        enqueues an animal to the cats or dogs queues based on animal type
        """
        if animal.type == 'cat':
            self.cats.enqueue(animal)
        elif animal.type == 'dog':
            self.dogs.enqueue(animal)
        
    
    def dequeue(self, pref = None):
        """
        returns the first cat or dog in queue, based on pref
        """
        if pref == 'cat':
            return self.cats.dequeue()
        elif pref == 'dog':
            return self.dogs.dequeue()


class Cat:
    """
    Cat class
    """
    def __init__(self, name):
        self.name = name
        self.type = 'cat'

class Dog:
    """
    Dog class
    """
    def __init__(self, name):
        self.name = name
        self.type = 'dog'