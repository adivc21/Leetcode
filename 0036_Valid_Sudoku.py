class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        N = 9
        
        # Bitmasks for each row, column, and box
        rows = [0] * N
        cols = [0] * N
        boxes = [0] * N
        
        for row in range(N):
            for col in range(N):
                
                if board[row][col] == ".":
                    continue
                    
                # Position to be bitmasked
                pos_in_bitmask = int(board[row][col]) - 1
                    
                if rows[row] & (1<<pos_in_bitmask):
                    return False
                rows[row] |= (1<<pos_in_bitmask)
                
                if cols[col] & (1<<pos_in_bitmask):
                    return False
                cols[col] |= (1<<pos_in_bitmask)
        
                # Calculating the index of the box
                box = (row//3)*3 + col//3
                
                if boxes[box] & (1<<pos_in_bitmask):
                    return False
                boxes[box] |= (1<<pos_in_bitmask)
                
        return True
        