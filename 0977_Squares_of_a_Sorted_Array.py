class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # # -----x-----x-----
        # # Solution 1 - One pass
        # # Time complexity = O(n)
        # # Space complexity = O(n)
                
        n = right = len(nums)-1
        left = 0
        res = [0] * len(nums)
        
        while left <= right:
            
            if abs(nums[right]) > abs(nums[left]):
                res[n] = nums[right] * nums[right]
                right -= 1
            else:
                res[n] = nums[left] * nums[left]
                left += 1
                
            n -= 1
            
        return res
        # # -----x-----x-----
