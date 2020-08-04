from fizz_buzz_tree import __version__
from fizz_buzz_tree.fizz_buzz_tree import Node, BinarySearchTree, BinaryTree


def test_version():
    assert __version__ == '0.1.0'


def test_imports():
    BinarySearchTree
    BinaryTree
    Node


def test_newtree():
    tree = BinarySearchTree()
    tree.add(15)
    tree.add(5)
    tree.add(3)
    tree.add(1)
    tree.add(35)
    tree.add(30)
    tree.add(9)
    tree.add(6)
    tree.add(41)
    tree.add(3)
    #assert tree.breadth_first() == [15, 5, 35, 3, 9, 30, 41, 1, 3, 6]
    assert tree.fizzbuzztree() == ['FizzBuzz', 'Buzz', 'Buzz', 'Fizz', 'Fizz', 'FizzBuzz', 'N', 'N', 'Fizz', 'Fizz']


# def logic(self, node):
        
        
#         #new_value = int(node.value)
#         if int(node.value) % 15 == 0:
#             self.newoutput.append('FizzBuzz')
#         elif int(node.value) % 3 == 0:
#             self.newoutput.append('Fizz')
#         elif int(node.value) % 5 == 0:
#             self.newoutput.append('Buzz')
#         else:
#             self.newoutput.append('N')

#         return self.newoutput

#     def fizzbuzztree(self):
#         newtree = BinarySearchTree()
#         queue, newqueue = [], []
#         queue.append(self.root)
#         newtree.add(self.root)

#         while queue:
#             node = queue.pop(0)
            
#             self.logic(node)

#             if node.left:
#                 self.logic(node.left)
                
#                 queue.append(node.left)
#                 newqueue.append(node.left)

#             if node.right:
#                 self.logic(node.right)
                    
#                 queue.append(node.right)
#                 newqueue.append(node.right)
                
#             if not queue:
#                 break

#         return self.newoutput