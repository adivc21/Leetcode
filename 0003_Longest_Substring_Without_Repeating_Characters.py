class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # # -----x-----x-----
        # # Solution 1 - Local and Global longest substring length
        # # Time complexity = O(n^2)
        # # Space complexity = O(n)

        # global_substr_len = local_substr_len = 0
        # local_substr = ""
                
        # for i in range(len(s)):
        #     if s[i] in local_substr:
        #         index = s[i-1::-1].index(s[i])
        #         local_substr = s[i-index:i+1]
        #         local_substr_len = len(local_substr)
        #     else:
        #         local_substr += s[i]
        #         local_substr_len += 1
        #         global_substr_len = max(global_substr_len, local_substr_len)
                
        # return global_substr_len
        # # -----x-----x-----
        
        # # -----x-----x-----
        # # Solution 2 - Sliding window
        # # Time complexity = O(n)
        # # Space complexity = O(n)

        n = len(s)
        res = left = right = 0
        char_indices = dict()
                
        while right < n:
            char = s[right]
            
            if (char in char_indices
                and char_indices[char] >= left
                and char_indices[char] < right):
                    left = char_indices[char] + 1

            char_indices[s[right]] = right
            res = max(res, right-left+1)
            right += 1
            
        return res
        # # -----x-----x-----      
        