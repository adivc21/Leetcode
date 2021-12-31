# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if (head == None):
            return head
        
        while (head.val==val):
            head = head.next
            if (head == None):
                return head
        
        prev = head
        curr = head.next
        
        while (curr != None):
            if (curr.val==val):
                if (curr.next!=None):
                    prev.next = curr.next
                    curr = curr.next
                else:
                    prev.next = None
                    curr = curr.next
            else:
                prev = prev.next
                curr = curr.next

        return head
    