class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCharCount = collections.Counter(s)
        tCharCount = collections.Counter(t)
        
        if (len(s) != len(t)):
            return False
        else:
            for char in sCharCount:
                if sCharCount[char] != tCharCount[char]:
                    return False
        
        return True
            