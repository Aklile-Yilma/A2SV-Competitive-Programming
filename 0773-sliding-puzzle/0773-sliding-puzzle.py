class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        row_len, col_len = len(board), len(board[0])          
        q = deque()
        directions = [1, 0, -1, 0, 1] 
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        
        def check(board):
            if board == [[1,2,3],[4,5,0]]:
                return True
            return False
        
        visited = set()
        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] == 0:
                    q.append(((r, c), board, 0))
                    visited.add(tuple(map(tuple, board)))
                    
        while q:
            (row, col), board, steps = q.popleft()
            
            if check(board):
                return steps
            
            for idx in range(len(directions)-1):
                new_row = row + directions[idx]
                new_col = col + directions[idx+1]
                if inbound(new_row, new_col):
                    new_board = [row[:] for row in board]
                    new_board[new_row][new_col], new_board[row][col] = new_board[row][col], new_board[new_row][new_col]
                    if tuple(map(tuple, new_board)) not in visited:
                        q.append(((new_row, new_col), new_board, steps+1))
                        visited.add(tuple(map(tuple, new_board)))
                        
                        
        return -1
        
