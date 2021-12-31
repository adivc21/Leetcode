# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        sentinel = ListNode(-101, head)
        prev = sentinel
        curr = sentinel.next
        
        while curr:
            if (curr.val == prev.val):
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
                
        return sentinel.next
        