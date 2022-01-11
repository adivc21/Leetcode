# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # # -----x-----x-----
        # # Solution 1 - One pass - Two pointers
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        sentinel = ListNode()
        sentinel.next = head
        slow = sentinel
        fast = sentinel.next.next
        
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next
            
        slow.next = slow.next.next
        return sentinel.next
        # # -----x-----x-----
    