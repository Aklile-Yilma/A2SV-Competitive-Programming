
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        source = [-1, -1]
        for row_idx in range(row):
            for col_idx in range(col):
                if grid[row_idx][col_idx] == 1:
                    source = [row_idx, col_idx]
                    break
                    
        def dfs(row, col, perimeter):
            if not inbound(row, col) or grid[row][col] == 0:
                return 1

            perimeter = 0
            visited.add((row, col))
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if (new_row, new_col) not in visited:
                    perimeter += dfs(new_row, new_col, perimeter)
                    
            return perimeter

        return dfs(source[0],source[1], 0)

