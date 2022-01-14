class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        # # -----x-----x-----
        # # Solution 1 - Two pass
        # # Time complexity = O(n^2)
        # # Space complexity = O(1)

        checked = set()
        
        for n in arr:
            if (n*2) in checked:
                return True
            elif n%2==0 and n//2 in checked:
                return True
            else:
                checked.add(n)
            
        return False
        # # -----x-----x-----
