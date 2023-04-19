class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        click_row, click_col = click
        
        if board[click_row][click_col] == "M":
            board[click_row][click_col] = "X"
            return board
        
        row_len, col_len = len(board), len(board[0])
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        directions = [(1, 0), (0,1), (-1, 0), (0,-1), (1,1),(-1,-1), (1,-1), (-1,1)]
        
        
        def dfs(row, col):
            #basecase
            if board[row][col] != "E":
                return
            
            count = 0
            #count number of mines
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row,new_col) and board[new_row][new_col] == "M":
                    count += 1
                    
            if count:
                board[row][col] = str(count)
                return
            
            board[row][col] = "B"
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col):
                    dfs(new_row, new_col)
                    
            return
        
        dfs(click_row, click_col)
        
        return board
                
            
            
            
            
            