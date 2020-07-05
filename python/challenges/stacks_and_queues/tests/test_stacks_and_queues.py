import pytest
from stacks_and_queues import __version__
from stacks_and_queues.stacks_and_queues import Node, Stack, Queue

def test_version():
    assert __version__ == '0.1.0'


def test_node_exist():
    assert Node


def test_Stack_exist():
    assert Stack


def test_Queue_exist():
    assert Queue


# Can successfully push onto a stack
def test_push():
    stck1 = Stack()
    stck1.push(5)
    assert stck1.top.value == 5

# Can successfully push multiple values onto a stack
def test_push_multiple():
    stck2 = Stack()
    stck2.push(9)
    stck2.push(8)
    stck2.push(10)
    stck2.push(7)
    stck2.push(11)
    assert stck2.top.value == 11
    assert stck2.top.next.value == 7

# Can successfully pop off the stack
def test_pop_stack():
    stck2 = Stack()
    stck2.push(9)
    stck2.push(8)
    stck2.push(10)
    assert stck2.pop() == 10
    assert stck2.top.value == 8


# Can successfully empty a stack after multiple pops
def test_pop_to_empty():
    stck2 = Stack()
    stck2.push(9)
    stck2.push(8)
    stck2.push(10)
    stck2.push(11)
    stck2.pop()
    stck2.pop()
    stck2.pop()
    stck2.pop()
    assert stck2.top == None
    assert stck2.is_empty() == True

# Can successfully peek the next item on the stack
def test_peek_stack():
    stck2 = Stack()
    stck2.push(9)
    stck2.push(8)
    stck2.push(10)
    assert stck2.peek() == 10
    
# Can successfully instantiate an empty stack
def test_instantiate_empty_stack():
    stck = Stack()
    assert stck.top == None
    assert stck.is_empty() == True

# Calling pop or peek on empty stack raises exception
def test_peek_from_empty():
    stck = Stack()
    assert stck.is_empty() == True
    with pytest.raises(AttributeError): 
        stck.peek()

def test_pop_from_empty():
    stck = Stack()
    assert stck.is_empty() == True
    with pytest.raises(AttributeError): 
        stck.peek()

# Can successfully enqueue into a queue
def test_enqueue():
    q = Queue()
    q.enqueue(7)
    assert q.front.value == 7
    assert q.rear.value == 7

# Can successfully enqueue multiple values into a queue
def test_enqueue_multiple():
    q1 = Queue()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.enqueue(4)
    q1.enqueue(5)
    assert q1.front.value == 1
    assert q1.front.next.value == 2
    assert q1.rear.value == 5

# Can successfully dequeue out of a queue the expected value
def test_dequeue():
    q2 = Queue()
    q2.enqueue(7)
    q2.enqueue(5)
    q2.enqueue(3)
    q2.enqueue(1)
    assert q2.rear.value == 1
    assert q2.dequeue() == 7
    assert q2.front.value == 5

# Can successfully peek into a queue, seeing the expected value
def test_peek_queue():
    q3 = Queue()
    q3.enqueue(1)
    q3.enqueue(3)
    q3.enqueue(5)
    q3.enqueue(7)
    assert q3.peek() == 1
    assert not q3.is_empty()

# Can successfully empty a queue after multiple dequeues
def test_dequeue_multiple():
    q4 = Queue()
    q4.enqueue(7)
    q4.enqueue(5)
    q4.enqueue(3)
    q4.enqueue(1)
    q4.dequeue()
    q4.dequeue()
    q4.dequeue()
    q4.dequeue()
    assert q4.front == None
    assert q4.rear == None
    assert q4.is_empty()
    
# Can successfully instantiate an empty queue
def test_instantiate_empty_queue():
    q5 = Queue()
    assert q5.front == None
    assert q5.is_empty() == True

# Calling dequeue or peek on empty queue raises exception
def test_dequeue_from_empty():
    q6 = Queue()
    assert q6.is_empty()
    with pytest.raises(AttributeError): 
        q6.dequeue()


def test_peek_queue_from_empty():
    q7 = Queue()
    assert q7.is_empty()
    with pytest.raises(AttributeError): 
        q7.peek()
