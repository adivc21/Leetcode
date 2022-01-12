class Solution:
    def maxPower(self, s: str) -> int:
        
        # # -----x-----x-----
        # # Solution 1 - One pass
        # # Time complexity = O(n)
        # # Space complexity = O(1)
                
        local_count = global_count = 0
        char = None
        
        for c in s:
            if c == char: local_count += 1
            else:
                global_count = max(global_count, local_count)
                char = c
                local_count = 1
                
        return max(global_count, local_count)
        # # -----x-----x-----    
