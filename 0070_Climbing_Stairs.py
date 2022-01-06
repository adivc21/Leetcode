class Solution:
    def climbStairs(self, n: int) -> int:
        
        # # -----x-----x-----
        # # Solution 1 - Fibonacci series
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        preceding = 1
        succeeding = 2
        
        if n==1: return preceding
        
        for i in range(2, n):
            temp = succeeding
            succeeding += preceding
            preceding = temp
            
        return succeeding
        # # -----x-----x-----
        