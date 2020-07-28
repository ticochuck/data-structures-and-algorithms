import pytest
from tree.tree import Node, BinaryTree, BinarySearchTree


def test_node_exists():
    assert Node


def test_BinaryTree_exists():
    BinaryTree


def test_BinarySearchTree():
    BinarySearchTree


# Can successfully instantiate an empty tree
def test_instantiate_empty_tree():
    bst = BinarySearchTree()
    assert bst


# Can successfully instantiate a tree with a single root node
def test_instantiate_tree_with_single_node():
    bst = BinarySearchTree()
    bst.add(1)
    assert bst
    assert bst.root.value == 1


# Can successfully add a left child and right child to a single root node
def test_left_right_children():
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(9)
    bst.add(11)
    assert bst.root.value == 10
    assert bst.root.left.value == 9
    assert bst.root.right.value == 11
    

# Can successfully return a collection from a preorder traversal
def test_traverse_preorder():
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(8)
    bst.add(17)
    bst.add(23)
    bst.add(3)
    bst.add(-1)
    bst.add(50)
    bst.add(34)
    assert bst.pre_order() == [10, 8, 3, -1, 17, 23, 50, 34]


# Can successfully return a collection from an inorder traversal
def test_traverse_inorder():
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(8)
    bst.add(17)
    bst.add(23)
    bst.add(3)
    bst.add(-1)
    bst.add(50)
    bst.add(34)
    assert bst.in_order() == [-1, 3, 8, 10, 17, 23, 34, 50]

def test_traverse_inorder2():
    bst = BinarySearchTree()
    bst.add(2)
    bst.add(7)
    bst.add(5)
    bst.add(2)
    bst.add(6)
    bst.add(9)
    bst.add(5)
    bst.add(11)
    bst.add(4)
    assert bst.in_order() == [2, 2, 4, 5, 5, 6, 7, 9, 11]


# Can successfully return a collection from a postorder traversal
def test_traverse_postorder():
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(8)
    bst.add(17)
    bst.add(23)
    bst.add(3)
    bst.add(-1)
    bst.add(50)
    bst.add(34)
    assert bst.post_order() == [-1, 3, 8, 34, 50, 23, 17, 10]
    assert bst.max_value() == 50


def test_max_value():
    bst = BinarySearchTree()
    bst.add(2)
    bst.add(7)
    bst.add(5)
    bst.add(2)
    bst.add(6)
    bst.add(9)
    bst.add(5)
    bst.add(11)
    bst.add(4)
    assert bst.max_value() == 11

