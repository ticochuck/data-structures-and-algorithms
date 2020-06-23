from challenges.linked_list.linked_list.linked_list import *


@staticmethod
    def merge_lists(ll1, ll2):
        

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


print(LinkedList.merge_lists([1,3,2], [5,9,4]))
