import pytest
from stacks_and_queues import __version__
from stacks_and_queues.stacks_and_queues import Node, Stack

def test_version():
    assert __version__ == '0.1.0'


def test_node_exist():
    assert Node


def test_Stack_exist():
    assert Stack


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
def test_pop():
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
def test_peek():
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
@pytest.mark.skip
def test_pop_from_empty():
    stck = Stack()
    assert stck.is_empty() == True
    actual = stck.peek()
    expected = 'AttributeError: The stack is Empty'
    assert actual == expected

# Can successfully enqueue into a queue
# Can successfully enqueue multiple values into a queue
# Can successfully dequeue out of a queue the expected value
# Can successfully peek into a queue, seeing the expected value
# Can successfully empty a queue after multiple dequeues
# Can successfully instantiate an empty queue
# Calling dequeue or peek on empty queue raises exception


