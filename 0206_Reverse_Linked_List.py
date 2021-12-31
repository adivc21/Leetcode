# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if (head == None):
            return head
        
        prev = head
        if (head.next == None):
            return head
        else:
            curr = head.next
            prev.next = None
            
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
            
        return prev
            