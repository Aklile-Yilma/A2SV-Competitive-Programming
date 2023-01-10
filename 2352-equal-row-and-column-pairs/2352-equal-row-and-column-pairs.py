from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        
        col_length = len(grid[0])
        row_length = len(grid)
        pairs = 0
        grid_map = {}
        
        for row in grid:
            row_tuple = tuple(row)
            
            if(row_tuple in grid_map):
                grid_map[row_tuple] += 1
            else:
                grid_map[row_tuple] = 1        
        
    
        for row_idx in range(row_length):
            curr_col = []
            for col_idx in range(col_length):
                curr_col.append(grid[col_idx][row_idx])
                
                                
            if(tuple(curr_col) in grid_map):
                pairs += grid_map[tuple(curr_col)]
                
        return pairs
                
                
            
                
                
                