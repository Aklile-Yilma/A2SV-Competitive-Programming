class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        DICE = 6
        destination = n*n
        
        def mapToIndex(num):
            #row index
            row = math.ceil(num / n)
            #col index
            #even rows are reversed
            if row % 2 == 0:
                col = n-(num % n)
                if col == n:
                    col = 0
            else:
                col = (num % n)
                if col == 0:
                    col = n - 1
                else:
                    col -= 1

            return (n-row, col)
        
        
        q = deque()
        visited = {1}        
        row, col = mapToIndex(1)
        if board[row][col] != -1:
             if board[row][col] not in visited:
                q.append((board[row][col], 0))
                visited.add(board[row][col])
        else:
            q.append((1, 0))            
                 
        while q:
            num, step = q.popleft()
            if num == destination:
                return step
            
            for d in range(1, DICE+1):
                new_num = num+d
                if new_num < destination + 1:
                    row, col = mapToIndex(new_num)
                    curr_step = 0
                    if board[row][col] != -1:
                        if board[row][col] not in visited:
                            q.append((board[row][col], step + 1))
                            visited.add(board[row][col])
                            visited.add(new_num)
                    else:
                        if new_num not in visited:
                            q.append((new_num, step+1))
                            visited.add(new_num)
                        
        return -1