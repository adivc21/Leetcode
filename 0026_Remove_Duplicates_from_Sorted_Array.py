class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # # -----x-----x-----
        # # Solution 1 - Modifying in place
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        if not nums:
            return 0 
    
        m = 0
        
        for i in range(len(nums)):
            if nums[m] != nums[i]:
                m += 1
                nums[m] = nums[i]
                
        return m+1
        # # -----x-----x-----
