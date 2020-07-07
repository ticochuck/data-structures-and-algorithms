class Node:
    """
    Node class
    """
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class PseudoQueue:
    """
    standard queue class
    """
    def __init__(self):
        # self.front = None
        # self.rear = None
        self.stck1 = Stack()
        self.stck2 = Stack()
    
    def __len__(self):
        return len(self.stck1)

    def enqueue(self, value):
        
        while self.stck1.top:
            self.stck2.push(self.stck1.pop())
            self.stck1.pop()
        
        self.stck1.push(value)

        while self.stck2.top:
            self.stck1.push(self.stck2.pop())
            self.stck2.pop()


    def dequeue(self):
        if len(self.stck1) == 0:
            print('The queue is Empty')

        return self.stck1.pop()
        


class Stack:
    """
    Stack Class
    """
    def __init__(self):
        self.top = None
    
    def push(self, value):
        """
        Adds to the top of the stack
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    

    def pop(self):
        """
        Removes the top node of the stack.
        Returns its value
        """
        if self.top:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        else:
            raise AttributeError('Stack is Empty')

    def peek(self):
        """
        Returns the value of the top node of the Stack.
        """
        if self.top:
            return self.top.value
        else:
            raise AttributeError('Stack is Empty')



tss = PseudoQueue()
tss.stck1.push(1)
tss.stck1.push(2)
tss.stck1.push(3)

print(tss.stck1.top.value)
print(tss.stck1.top.next.value)
print(tss.stck1.top.next.next.value)
print(tss.stck1.top.next.next.next)

# print(tss.front)
tss.enqueue(3)
tss.enqueue(4)
tss.enqueue(5)
print(tss.front.value)
print(tss.rear.value)


