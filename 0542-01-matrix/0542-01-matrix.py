class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        row_len, col_len = len(mat), len(mat[0])           
        inbound =  lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = deque()
        visited = set()
        
        for row in range(row_len):
            for col in range(col_len):
                if mat[row][col] == 0:
                    visited.add((row, col))
                    q.append((row, col))
                    
        while q:
            (row, col) = q.popleft()
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change    
                if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                    mat[new_row][new_col] = mat[row][col] + 1
                    visited.add((new_row, new_col))
                    q.append((new_row, new_col))
                    
        return mat

                                        
                
                
        