class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        row_len, col_len = len(isConnected), len(isConnected[0])
        visited = set()
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        count = 0
        
        def dfs(row, col):
                
            for col in range(col_len):
                new_row, new_col = row, col
                if inbound(row, col) and (new_row, new_col) not in visited and isConnected[row][col] != 0:
                    visited.add((new_row, new_col))
                    dfs(new_col, new_row)
            
            return
        
        for row in range(row_len):
            for col in range(col_len):
                if (row,col) not in visited and isConnected[row][col] != 0:
                    visited.add((row, col))
                    count += 1
                    dfs(row, col)
                    
        return count
            
            
            