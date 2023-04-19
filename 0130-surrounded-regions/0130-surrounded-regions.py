class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_len, col_len = len(board), len(board[0])
        directions = [1, 0, -1, 0, 1]
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
                
        def dfs(row, col):
            board[row][col] = "T"
            for idx in range(len(directions)-1):
                new_row = row + directions[idx]
                new_col = col + directions[idx+1]
                if inbound(new_row, new_col) and board[new_row][new_col] == "O":
                    dfs(new_row, new_col)
            return
        
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == "O" and (row in [0, row_len-1] or col in [0, col_len-1]):
                    dfs(row, col)
                    
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "T":
                    board[row][col] = "O"
                    
        
                    
        
                    
                    
        
                    
        
                    
                    
            
            