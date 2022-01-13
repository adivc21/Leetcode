class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        # # -----x-----x-----
        # # Solution 1 - One pass
        # # n=len(nums), k=worst-case number in nums
        # # Time complexity = O(n*log10(k))
        # # Space complexity = O(1)
        
        # count = 0
        
        # for n in nums:
        #     digits = 0
        #     while n:
        #         n //= 10
        #         digits +=1
                
            # if digits%2 == 0:
            #     count += 1
                
        # return count
        # # -----x-----x-----

        # # -----x-----x-----
        # # Solution 1 - One pass
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        count = 0
        
        for n in nums:
            if len(str(n))%2 == 0:
                count += 1
                
        return count
        # # -----x-----x-----
    