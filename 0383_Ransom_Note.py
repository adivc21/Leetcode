class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        charCount = collections.Counter(magazine)
        
        for char in ransomNote:
            if charCount[char] >=1:
                charCount[char] -= 1
            else:
                return False
            
        return True
        