class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        row_len, col_len = len(maze),len(maze[0])
        directions = [1, 0, -1, 0, 1]
        inbound =  lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        q = deque()
        q.append(((entrance[0], entrance[1]), 0))
        visited = {(entrance[0], entrance[1])}

        while q:
            (row, col), steps = q.popleft()

            if [row, col] != entrance and (row in [0, row_len-1] or col in [0, col_len-1]):
                return steps

            for idx in range(len(directions)-1):
                new_row = row + directions[idx]
                new_col = col + directions[idx+1]
                if inbound(new_row, new_col) and (new_row, new_col) not in visited and maze[new_row][new_col] != '+':
                    visited.add((new_row, new_col))
                    q.append(((new_row, new_col), steps + 1))

        return -1
