class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        charCount = dict()
        
        for char in s:
            if char in charCount:
                charCount[char] += 1
                
            else:
                charCount[char] = 1
                
        for i in range(len(s)):
            if charCount[s[i]] == 1:
                return i
        
        return -1
                