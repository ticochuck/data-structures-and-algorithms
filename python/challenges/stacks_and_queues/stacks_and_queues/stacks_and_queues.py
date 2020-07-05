class Node:
    """
    This is the Node class. 
    """
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class Stack:
    """
    Stack Class with a top property. 
    """
    def __init__(self):
        self.top = None
    
    def push(self, value):
        """
        Adds a new node with a given value to the top of the stack.
        """
        self.top = Node(value, self.top)

    
    def pop(self):
        """
        Removes the node from the top of the stack. 
        Returns the node’s value.
        """
        if self.top:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        else:
            raise AttributeError('The stack is Empty')


    def peek(self):
        """
        Returns the value of the node located on top of the stack.
        It raises exception when called on empty stack
        """
        if self.top:
            return self.top.value
        else:
            raise AttributeError('The stack is Empty')


    def is_empty(self):
        """
        Returns a boolean indicating whether or not the stack is empty.        
        """
        if self.top == None:
            return True
        else:
            return False


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


    def peek(self):
        """
        Returns the value of the node located in the front of the queue.
        It raises an exception when called on empty queue
        """
        if self.front:
            return self.front.value
        else:
            raise AttributeError('The queue is Empty')

    def is_empty(self):
        """
        Returns a boolean indicating whether or not the queue is empty
        """
        if self.front:
            return False
        else:
            return True

#q = Queue()
#q.peek()