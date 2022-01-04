class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # # -----x-----x-----
        # # Solution 1 - Gauss's formula to sum first n Natural Numbers
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        # n = len(nums)
        # first_n_natural_sum = (n*(n+1)) / 2
        # return int(first_n_natural_sum) - sum(nums)
        # # -----x-----x-----
        
        # # -----x-----x-----
        # # Solution 2 - Bit Manipulation using XOR
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        missing_number = n = len(nums)
        
        for i in range(n):
            missing_number ^= i ^ nums[i]
            
        return missing_number
        # # -----x-----x-----