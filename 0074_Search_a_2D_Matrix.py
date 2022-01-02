class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        for r in range(m):
            if not(target>=matrix[r][0] and target<=matrix[r][n-1]):
                continue
            for c in range(n):
                if matrix[r][c] == target: 
                    return True
                
        return False
    