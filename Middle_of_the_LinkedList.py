class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length =0
        #print(head)
        node = head
        #print(node)
        my_dict = dict()
        while(node != None):
            length += 1
            print(node.val)
            my_dict[length] = node
            node = node.next
        
        print("Length : ",length)
        #print(my_dict)
        middle = (length//2) + 1
        return my_dict[middle]