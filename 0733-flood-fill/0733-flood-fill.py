class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        row_len = len(image)
        col_len = len(image[0])
        initial_color = image[sr][sc]
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def inbound(row, col):
            
            return 0 <= row < row_len and 0 <= col < col_len
        
        def dfs(row, col):
            
            #visited this before
            if image[row][col] == color:
                return
            
            image[row][col] = color
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if inbound(new_row, new_col) and image[new_row][new_col] == initial_color:
                    dfs(new_row, new_col)
            return
        
        dfs(sr, sc)
        
        return image
        