class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        col_len = len(grid[0])
        prefix_row1 = [grid[0][0]]
        prefix_row2 = [grid[1][0]]

        for col in range(1, col_len):
            prefix_row1.append(prefix_row1[-1] + grid[0][col]) 
            prefix_row2.append(prefix_row2[-1] + grid[1][col]) 
                        
        points = float('inf')
        
        for col in range(col_len):
            top = prefix_row1[-1] - prefix_row1[col]
            bottom = prefix_row2[col-1] if col > 0 else 0
            secondRobot = max(top, bottom)
            points = min(points, secondRobot)
            
        return points
            
            
        
    
        
        
        