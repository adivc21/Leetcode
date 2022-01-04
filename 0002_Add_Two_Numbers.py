# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # # -----x-----x-----
        # # Solution 1 - Using another Linked List
        # # m=len(l1), n=len(l2)
        # # Time complexity = O(max(m, n))
        # # Space complexity = O(max(m, n))
        # carry = 0
        # result = ListNode()
        # temp = result
        
        # while l1 and l2:
        #     temp.val = (l1.val + l2.val + carry) % 10
        #     carry = (l1.val + l2.val + carry) // 10
        #     l1 = l1.next
        #     l2 = l2.next
        #     prev = temp
        #     temp.next = ListNode()
        #     temp = temp.next
            
        # if l1:
        #     while l1:
        #         temp.val = (l1.val + carry) % 10
        #         carry = (l1.val + carry) // 10
        #         l1 = l1.next
        #         prev = temp
        #         temp.next = ListNode()
        #         temp = temp.next
                
        # if l2:
        #     while l2:
        #         temp.val = (l2.val + carry) % 10
        #         carry = (l2.val + carry) // 10
        #         l2 = l2.next
        #         prev = temp
        #         temp.next = ListNode()
        #         temp = temp.next
                
        # if carry:
        #     temp.val = carry
        # else:
        #     prev.next = None
            
        # return result
        # # -----x-----x-----
        
        
        # # -----x-----x-----
        # # Solution 2 - Modifying existing Linked List
        # # m=len(l1), n=len(l2)
        # # Time complexity = O(max(m, n))
        # # Space complexity = O(max(1, (n-m)))
        carry = 0
        result = l1
        
        while l1 and l2:
            face_sum = l1.val + l2.val + carry
            l1.val = face_sum % 10
            carry = face_sum // 10
            prev = l1
            l1 = l1.next
            l2 = l2.next
            
        if l1:
            while l1:
                face_sum = l1.val + carry
                l1.val = face_sum % 10
                carry = face_sum // 10
                prev = l1
                l1 = l1.next
            
        if l2:
            while l2:
                prev.next = ListNode()
                l1 = prev.next
                face_sum = l2.val + carry
                l1.val = face_sum % 10
                carry = face_sum // 10
                prev = l1
                l2 = l2.next
                
        if carry:
            prev.next = ListNode()
            prev.next.val = carry

        return result
        # # -----x-----x-----
        