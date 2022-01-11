# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # # -----x-----x-----
        # # Solution 1 - One pass - Two pointers
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        slow = head
        fast = head.next
        
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next
            
        return slow
        # # -----x-----x-----
