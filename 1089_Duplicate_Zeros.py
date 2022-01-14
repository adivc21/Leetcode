class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # # -----x-----x-----
        # # Solution 1 - Two pass
        # # Time complexity = O(2n)
        # # Space complexity = O(1)
        
        zero_count = 0
        count = 0
        n = len(arr)
        
        for num in arr:
            if not num:
                zero_count += 1
                count += 2
            else:
                count += 1
            
            if count == n: break
            elif count > n: 
                count -= 2
                arr[count] = 0
                zero_count -= 1
                break
                
        count -= 1
        while zero_count:
            if arr[count-zero_count]:
                arr[count] = arr[count-zero_count]
                count -= 1
            else:
                arr[count] = arr[count-1] = 0
                zero_count -= 1
                count -= 2
        # # -----x-----x-----
