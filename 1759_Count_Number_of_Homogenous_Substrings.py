class Solution:
    def countHomogenous(self, s: str) -> int:
        
        # # -----x-----x-----
        # # Solution 1 - One pass
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        global_count = 0
        local_count = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                local_count += 1
            else:
                global_count += (local_count*(local_count+1)) // 2
                local_count = 1
            
        global_count += (local_count*(local_count+1)) // 2
            
        return global_count % ((10**9)+7)
        # # -----x-----x-----
