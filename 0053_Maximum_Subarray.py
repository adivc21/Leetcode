class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        The following is Kadane's Algorithm to
        find the find the contiguous subarray
        which has the largest sum and return its sum
        '''
        local_max_sum = nums[0]
        global_max_sum = nums[0]
        
        for i in range(1, len(nums)):
            if (local_max_sum + nums[i] > nums[i]):
                local_max_sum = local_max_sum + nums[i]
            else:
                local_max_sum = nums[i]
            
            if(local_max_sum > global_max_sum):
                global_max_sum = local_max_sum
                
        return global_max_sum
        