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
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value


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

