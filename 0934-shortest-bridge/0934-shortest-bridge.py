class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        directions = [1, 0, -1, 0, 1]
        #find one
        source = ()
        found = False
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1:
                    source = (row, col)
                    found = True
                    break   
            if found:
                break
        
        print(source)
        #find all neightbors of 1
        q = deque()
        q.append(source)
        visited = {source}
        while q:
            row, col = q.popleft()
            for idx in range(len(directions)-1):
                new_row = row+directions[idx]
                new_col = col+directions[idx+1]
                if inbound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                    q.append((new_row, new_col))
                    visited.add((new_row, new_col))
                    
        #do bfs from all the nodes of the first island
        sources = list(visited)
        for source in sources:
            q.append((source, 0))
        while q:
            (row, col), step = q.popleft()
            
            #return shortest path to find 1
            
            for idx in range(len(directions)-1):
                new_row = row+directions[idx]
                new_col = col+directions[idx+1]
                if inbound(new_row, new_col) and (new_row, new_col) not in visited:
                    if grid[new_row][new_col] == 1:
                        return step
                    q.append(((new_row, new_col), step+1))
                    visited.add((new_row, new_col))
                    
        
        
        