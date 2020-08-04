class Node:
    """
    This is the Node class. 
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

 
class BinaryTree:
    def __init__(self):
        self.root = None
        self.newoutput = None
    
    def logic(self, node):
        
        newoutput = []
        
        new_value = int(node.value)
        if new_value % 15 == 0:
            newoutput.append('FizzBuzz')
        elif new_value % 3 == 0:
            newoutput.append('Fizz')
        elif new_value % 5 == 0:
            newoutput.append('Buzz')
        else:
            newoutput.append('N')

        return newoutput


    def fizzbuzztree(self):
        newtree = BinarySearchTree()
        newoutput, queue, newqueue = [], [], []
        queue.append(self.root)
        newtree.add(self.root)

        while queue:
            node = queue.pop(0)
            
            if int(node.value) % 15 == 0:
                newoutput.append('FizzBuzz')
            elif int(node.value) % 3 == 0:
                newoutput.append('Fizz')
            elif int(node.value) % 5 == 0:
                newoutput.append('Buzz')
            else:
                newoutput.append('N')

            if node.left:
                if int(node.left.value) % 15 == 0:
                    newtree.root.left = 'FizzBuzz'
                elif int(node.left.value) % 3 == 0:
                    newtree.root.left = 'Fizz'
                elif int(node.left.value) % 5 == 0:
                    newtree.root.left = 'Buzz'
                else:
                    newtree.root.left = 'N'
                
                queue.append(node.left)
                newqueue.append(node.left)

            if node.right:
                if int(node.right.value) % 15 == 0:
                    newtree.root.left = 'FizzBuzz'
                elif int(node.right.value) % 3 == 0:
                    newtree.root.left = 'Fizz'
                elif int(node.right.value) % 5 == 0:
                    newtree.root.left = 'Buzz'
                else:
                    newtree.root.left = 'N'
                    
                queue.append(node.right)
                newqueue.append(node.right)
                
            if not queue:
                break

        print('Newoutput: ', newoutput)
        return newoutput


        

class BinarySearchTree(BinaryTree):
    
    def add(self, value):
        """
        Add a node to the Binary Tree
        """
        def walk(node, node_to_add):
            if not node:
                return

            if node_to_add.value < node.value:
                if not node.left:
                    node.left = node_to_add
                else:
                    walk(node.left, node_to_add)
            else:
                if not node.right:
                    node.right = node_to_add
                else:
                    walk(node.right, node_to_add)

        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return
        
        walk(self.root, new_node)
     
     
    
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

tree.fizzbuzztree()
