class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # # -----x-----x-----
        # # Solution 1 - Assigning indices that match
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        # if not nums: return 0
        
        # m = len(nums)-1
        # i = 0
        
        # while i<len(nums):
        #     if nums[i] == val:
        #         nums[i] = nums[m]
        #         nums[m] = -1
        #         m -= 1
        #         continue
        #     i += 1
                
        # return m+1
        # # -----x-----x-----
        
        # # -----x-----x-----
        # # Solution 1 - Assigning indices that don't match
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        m = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[m] = nums[i]
                m += 1
                
        return m
        # # -----x-----x-----