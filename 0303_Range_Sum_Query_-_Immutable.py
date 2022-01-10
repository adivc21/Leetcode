# # -----x-----x-----
# # Solution 1 - Caching
# # Time complexity = O(n)
# # Space complexity = O(n+1)

class NumArray:

    def __init__(self, nums: List[int]):
        
        self.sums = list()
        self.sums.append(0)
        
        for i in range(len(nums)):
            self.sums.append(self.sums[i] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        
        return self.sums[right+1] - self.sums[left]
# # -----x-----x-----
    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
