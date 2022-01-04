class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Return true if the number of elements in nums
        is greater than the number of unique elements
        in nums
        '''
        # # -----x-----x-----
        # # Solution 1 - Length of Set
        # # Time complexity = O(n)
        # # Space complexity = O(n)
        # return len(nums) > len(set(nums))
        # # -----x-----x-----

        # # -----x-----x-----
        # # Solution 2 - Set
        # # Time complexity = O(n)
        # # Space complexity = O(n)
        # nums_set = set()
        
        # for n in nums:
        #     if n in nums_set:
        #         return True
        #     nums_set.add(n)
            
        # return False
        # # -----x-----x-----
        
        # # -----x-----x-----
        # # Solution 3 - Sort
        # # Time complexity = Depends on sorting algorithm used
        # # Space complexity = O(1)
        nums.sort()
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: return True
        return False
        # # -----x-----x-----
        