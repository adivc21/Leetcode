class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # # -----x-----x-----
        # # Solution 1 - Binary search
        # # Time complexity = O(log(n))
        # # Space complexity = O(1)
        
        left = 0
        right = len(nums)-1
        mid = (left + right) // 2
        
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
                mid = (left + right) // 2
            else:
                left = mid + 1
                mid = (left + right) // 2
            
        return left
        # # -----x-----x-----
    