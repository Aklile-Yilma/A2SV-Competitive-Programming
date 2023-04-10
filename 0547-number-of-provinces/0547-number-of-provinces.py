class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        row_len, col_len = len(isConnected), len(isConnected[0])
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        count = 0
        
        def dfs(row, col):
                
            for col in range(col_len):
                new_row, new_col = row, col
                if inbound(row, col) and  isConnected[row][col] != 0:
                    isConnected[row][col] = 0
                    dfs(new_col, new_row)
            
            return
        
        for row in range(row_len):
            for col in range(col_len):
                if isConnected[row][col] != 0:
                    count += 1
                    isConnected[row][col] = 0
                    dfs(row, col)
                    
        return count
            
            
            