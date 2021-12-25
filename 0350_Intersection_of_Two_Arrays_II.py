class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()
        count = collections.Counter(nums1)
        
        for num in nums2:
            if num in count and count[num]>0:
                result.append(num)
                count[num]-=1
                
        return result
        