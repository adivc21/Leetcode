class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # # -----x-----x-----
        # # Solution 1 - Local and Global longest substring length
        # # Time complexity = O(n^2)
        # # Space complexity = O(n)

        global_substr_len = local_substr_len = 0
        local_substr = ""
                
        for i in range(len(s)):
            if s[i] in local_substr:
                index = s[i-1::-1].index(s[i])
                local_substr = s[i-index:i+1]
                local_substr_len = len(local_substr)
            else:
                local_substr += s[i]
                local_substr_len += 1
                global_substr_len = max(global_substr_len, local_substr_len)
                
        return global_substr_len
        # # -----x-----x-----