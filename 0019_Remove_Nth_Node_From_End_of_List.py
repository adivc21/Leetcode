# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # # -----x-----x-----
        # # Solution 1 - Two Pass
        # # Time complexity = O(2n)
        # # Space complexity = O(1)
        
        # length = 0
        # sentinel = ListNode()
        # sentinel.next = head
        # curr = sentinel
        
        # while curr:
        #     length += 1
        #     curr = curr.next
            
        # length -= n+1
        # curr = sentinel
        
        # while length:
        #     curr = curr.next
        #     length -= 1
            
        # if curr.next.next:
        #     curr.next = curr.next.next
        # else:
        #     curr.next = None
        
        # return sentinel.next
        # # -----x-----x-----
        
        # # -----x-----x-----
        # # Solution 1 - One Pass - Two Pointers
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        sentinel = ListNode()
        sentinel.next = head
        curr = head
        
        while n:
            curr = curr.next
            n -= 1
        
        prev_of_removed_node = sentinel
        
        while curr:
            curr = curr.next
            prev_of_removed_node = prev_of_removed_node.next
            
        prev_of_removed_node.next = prev_of_removed_node.next.next
        
        return sentinel.next
        # # -----x-----x-----        
    