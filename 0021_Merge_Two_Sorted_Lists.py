# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode(-101)
        traverse = result
        
        while (list1 and list2):
            if (list1.val < list2.val):
                traverse.next = list1
                list1 = list1.next
                traverse = traverse.next
            else:
                traverse.next = list2
                list2 = list2.next
                traverse = traverse.next
            
        if (list1):
            traverse.next = list1
            
        if (list2):
            traverse.next = list2
                
        return result.next
    