from linked_list import LinkedList


class MergeLists:
    """
    Takes to linked lists and merges them using alternative values
    """

    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return f'{self.head}'

    def merge_lists(ll1, ll2):
        """Takes in 2 linked list and merges the 2 alternating values. 
        
        Args:
            ll1 ([Linkedlist])
            ll2 ([Linkedlist])

        Returns:
            Returns head of merged list
        """

        if not ll1.head:
            return ll2.head
        elif not ll2.head:
            return ll1.head
        
        current1, current2 = ll1.head, ll2.head
        while current1:
            if current2:
                tmp1, current1.next_node = current1.next_node, current2
                if tmp1:
                    tmp2, current2.next_node = current2.next_node, tmp1
                if not tmp2:
                    break
                
                current1, current2 = tmp1, tmp2
        return ll1.head


ll1 = LinkedList()
ll1.insert(2)
ll1.insert(3)
ll1.insert(1)
print(ll1.head)
ll2 = LinkedList()
#LinkedList.merge_lists([1,3,2], [5,9,4])
