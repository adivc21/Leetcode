class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # # -----x-----x-----
        # # Solution 1 - One pass
        # # Time complexity = O(n)
        # # Space complexity = O(1)
        
        n = len(arr) - 1
        max_val = arr[n]
        arr[n] = -1
        
        while n:
            prev = arr[n-1]
            arr[n-1] = max_val
            max_val = max(max_val, prev)
            n -= 1
            
        return arr        
        # # -----x-----x-----
