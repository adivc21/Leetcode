class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        # # -----x-----x-----
        # # Solution 1 - Two pointers, starting from the left
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        # slow = 0
        
        # for fast in range(len(nums)):
        #     if nums[fast]%2 == 0:
        #         nums[slow], nums[fast] = nums[fast], nums[slow]
        #         slow += 1

        # return nums
        # # -----x-----x-----
        
        # # -----x-----x-----
        # # Solution 2 - Two pointers, starting from different ends
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left]%2 > nums[right]%2:
                nums[left], nums[right] = nums[right], nums[left]
                
            if not nums[left]%2:
                left += 1
                
            if nums[right]%2:
                right -= 1
        
        return nums
        # # -----x-----x-----
