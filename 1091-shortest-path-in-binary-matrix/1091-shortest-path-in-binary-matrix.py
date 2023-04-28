class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        row_len, col_len = len(grid), len(grid[0])
        inbound =  lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1],[1, -1], [-1, -1]]
        
        q = deque()
        q.append(((0,0), 1))
        visited = set((0, 0))
        

        while q:
            node, step = q.popleft()
            row, col = node
            if (row, col) == (row_len-1, col_len-1):
                return step

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if (new_row, new_col) not in visited and inbound(new_row, new_col) and grid[new_row][new_col] == 0:
                    visited.add((new_row, new_col))
                    q.append(((new_row, new_col), step + 1))
                    
        return -1
                
                
                    
        
        
        