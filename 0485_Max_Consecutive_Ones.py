class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # # -----x-----x-----
        # # Solution 1 - One pass
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        local_sum = global_sum = 0
        
        for i in nums:
            if i:
                local_sum += 1
            else:
                global_sum = max(global_sum, local_sum)
                local_sum = 0
                
        return max(global_sum, local_sum)
        # # -----x-----x-----
