class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # # -----x-----x-----
        # # Solution 1 - XOR
        # # XORing a number with itself results into a zero
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        # single_num = 0
        
        # for num in nums:
        #     single_num ^= num
            
        # return single_num
        # # -----x-----x-----
        
        # # -----x-----x-----
        # # Solution 2 - Sum and difference
        # # Formula: 2(a+b+c) - (a+a+b+c+c) = b
        # # Time complexity = O(2n)
        # # Space complexity = O(n)
        
        # return 2*sum(set(nums)) - sum(nums)
        # # -----x-----x-----
        
        # # -----x-----x-----
        # # Solution 3 - Using dictionary
        # # Time complexity = O(n^2)
        # # Space complexity = O(n)
        
        num_count = collections.Counter(nums)
        
        for n in nums:
            if num_count[n]==1: return n
        # # -----x-----x-----
        