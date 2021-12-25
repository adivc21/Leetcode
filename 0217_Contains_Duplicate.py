class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Return true if the number of elements in nums
        is greater than the number of unique elements
        in nums
        '''
        return len(nums) > len(set(nums))
        