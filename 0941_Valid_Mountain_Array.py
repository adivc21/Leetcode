class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        # # -----x-----x-----
        # # Solution 1 - One pass
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        length = len(arr)
        
        if length < 3:
            return False
        
        n = 0
        
        while n < length-1:
            if arr[n] < arr[n+1]: n += 1
            elif arr[n] == arr[n+1]: return False
            else: break
                    
        if n==0 or n==length-1: return False
        
        while n < length-1:
            if arr[n] > arr[n+1]: n += 1
            else: return False
            
        return True
        # # -----x-----x-----
