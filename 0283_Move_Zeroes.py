class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # -----x-----x-----
        # # Solution 1 - Modifying in place
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        z = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[z], nums[i] = nums[i], nums[z]
                z += 1
        # # -----x-----x-----            
