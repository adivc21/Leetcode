class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # # -----x-----x-----
        # # Solution 1 - One pass
        # # Time complexity = O(2n)
        # # Space complexity = O(2n)
        
        # n = len(nums)
        # num_set = set(nums)
        # res = list()
        
        # for i in range(1, len(nums)+1):
        #     if i not in num_set:
        #         res.append(i)
                
        # return res
        # # -----x-----x-----
        
        # # -----x-----x-----
        # # Solution 2 - In-place modification
        # # Time complexity = O(2n)
        # # Space complexity = O(n)
        
        # n = len(nums)
        # res = list()
        
        # for i in range(n):
        #     abs_val = abs(nums[i]) - 1
        #     if nums[abs_val]>0: nums[abs_val] *= -1
                
        # for i in range(1, n+1):
        #     if nums[i-1]>0: res.append(i)
                
        # return res
        # # -----x-----x-----       
        
        # # -----x-----x-----
        # # Solution 3 - Python one line solution
        # # Time complexity = O(3n)
        # # Space complexity = O(3n)
        
        return set(range(1, len(nums)+1)).difference(set(nums))
        # # -----x-----x-----       