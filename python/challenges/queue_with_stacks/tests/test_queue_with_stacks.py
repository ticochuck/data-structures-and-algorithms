import pytest
from queue_with_stacks import __version__
from queue_with_stacks.queue_with_stacks import PseudoQueue, Stack

def test_version():
    assert __version__ == '0.1.0'


def test_PseudoQueue_exists():
    PseudoQueue


def test_Stack_exists():
    Stack


def test_enqueue():
    pseudoq = PseudoQueue()
    pseudoq.enqueue(1)
    assert pseudoq.stck1.peek() == 1


def test_enqueue_2():
    pseudo = PseudoQueue()
    pseudo.enqueue(2)
    pseudo.enqueue(3)
    assert pseudo.stck1.peek() == 2


def test_dequeue():
    pseudo = PseudoQueue()
    pseudo.enqueue(1)
    pseudo.enqueue(2)
    pseudo.enqueue(3)
    pseudo.enqueue(4)
    pseudo.dequeue()
    assert pseudo.stck1.peek() == 2


def test_dequeue_2():
    pseudo = PseudoQueue()
    pseudo.enqueue(1)
    pseudo.enqueue(2)
    pseudo.enqueue(3)
    pseudo.enqueue(4)
    pseudo.dequeue()
    pseudo.dequeue()
    pseudo.dequeue()
    assert pseudo.stck1.peek() == 4


def test_dequeue_until_empty():
    pseudo = PseudoQueue()
    pseudo.enqueue(1)
    pseudo.enqueue(2)
    pseudo.enqueue(3)
    pseudo.enqueue(4)
    pseudo.dequeue()
    pseudo.dequeue()
    pseudo.dequeue()
    pseudo.dequeue()
    with pytest.raises(AttributeError): 
        pseudo.stck1.peek()