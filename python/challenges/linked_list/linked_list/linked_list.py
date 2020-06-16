class Node:
    """
    This is the Node class
    """

    def __init__(self, value, next_node = None):
        """
        This is to create a node with a value and a next reference

        Args:
            value : node value 
            next_node : reference to next node
        """
        
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return {'Value':{self.value}, 'Next Node':{self.next_node}}
        

    def __str__(self):
        return f"{self.value}, Next_Node={self.next_node}"


class LinkedList:
    """
    This is the class LinkedList
    """
    def __init__(self):
        """
        This is to initializa the LinkedList
        """
        self.head = None
    

    def __str__(self):
        """
        prints LinkedList 
        """
        return f"head: {self.head}"

    
    def insert(self, value):
        """
        Method to insert a node to the LinkedList.
        """
        node = Node(value)
        
        if self.head is not None:
            node.next_node = self.head
        self.head = node

    
    def includes(self, value):
        """
        Method to check in a Linked List includes a value.
        """

        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next_node
        
        return False
    
    def append(self, value):
        """
        Appends a new node to the end of a Linked List
        """
        node = Node(value)

        if self.head is Node:
            self.head = node
            return

        current = self.head

        while current.next_node is not None:
            current = current.next_node
        current.next_node = node

ll = LinkedList()

ll.insert('Saturday')
ll.insert('Friday')
ll.insert('Thursday')
ll.insert('Wednesday')
ll.insert('Tuesday')
ll.insert('Monday')
ll.insert('Sunday')

ll.append('March')
ll.append('February')
ll.append('January')

print(ll.head)

print(ll.includes('Saturday'))
print(ll.includes('November'))

print(Node(ll))
