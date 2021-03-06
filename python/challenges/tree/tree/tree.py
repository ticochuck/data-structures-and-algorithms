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
    
    
    def pre_order(self):
        """
        root, left, right
        """
        output = []

        def traverse(node):
            
            if not node:
                return
        
            output.append(node.value)
            traverse(node.left)
            traverse(node.right)
            
        traverse(self.root)

        print('Pre-order: ', output)
        return output

    def in_order(self):
        """
        left, root, right
        """
        
        output = []

        def traverse(node):
            
            if not node:
                return
            
            traverse(node.left)
            output.append(node.value)
            traverse(node.right)
        
        traverse(self.root)
        
        print('In Order: ', output)
        return output

    def post_order(self):
        """
        left, right, root
        """
        output = []

        def traverse(node):
            
            if not node:
                return
        
            traverse(node.left)
            traverse(node.right)
            output.append(node.value)
            
        traverse(self.root)

        print('Post-order: ', output)
        return output

# I used this for reference: 
# https://codereview.stackexchange.com/questions/191984/perform-bfs-on-a-binary-tree
    def breadth_first(self):
        
        output = []
        
        queue = []
        queue.append(self.root)
        
        while queue:
            node = queue.pop(0)
            output.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if not queue:
                break

        print('Breadth first: ', output)
        return output
        

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

    
    def contains(self, value):
        """
        Takes in a value, checks if the BST contians the value. 
        Returns True if it does, False if it doesn't
        """
        def search(node):
            if node:
                if node.value == value:
                    return True
        
                if node.value < value: 
                    return search(node.right) 
                if node.value > value: 
                    return search(node.left) 
            else:
                return False
            
        return search(self.root)


    def max_value(self):
        value = self.root.value
        def highest(node, value=0):
        
            if node:
                if node.value > value:
                    value = node.value
                highest(node.left, value)
                return highest(node.right, value)
            else:
                return value
    
        return highest(self.root, value)
    
               
bst = BinarySearchTree()
bst.add(10)
bst.add(8)
bst.add(17)
bst.add(23)
bst.add(3)
bst.add(-1)
bst.add(50)
bst.add(34)
print(bst.contains(-1))
print(bst.max_value())

bst.pre_order()
bst.in_order()
bst.post_order()
bst.breadth_first()

bt = BinaryTree()
root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.right = Node(9)
root.left.right.left = Node(5)
root.left.right.right = Node(11)
root.right.right.left = Node(4)
bt.root = root
bt.breadth_first()

