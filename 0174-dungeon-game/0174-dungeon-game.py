class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        row_len, col_len = len(dungeon), len(dungeon[0])
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        dst = (row_len-1, col_len-1)
        
        memo = {}
        def dfs(row, col):
            
            if (row, col) == dst:
                return dungeon[row][col] if dungeon[row][col] < 0 else 0
            
            if (row, col) in memo:
                return memo[(row, col)]
            
            curr = dungeon[row][col]
            move_right = curr + dfs(row, col+1) if inbound(row, col+1) else float('-inf')            
            move_down = curr + dfs(row+1, col) if inbound(row+1, col) else float('-inf')
            
            ans = max(move_right , move_down) 
            memo[(row, col)] = ans if ans < 0 else 0
            
            return memo[(row, col)]
        
        return abs(dfs(0, 0)) + 1
    
    