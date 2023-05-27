class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        seen = defaultdict(set)
        inbound = lambda row, col: 0 <= row < row_len and 0 <= col < col_len
        directions = [1, 0, -1, 0, 1]
        k = 0
        
        #find start node
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == '@':
                    start = (row, col)
                if grid[row][col].islower():
                    k += 1        
 
        q = deque()
        # (cur_row, cur_col, keys, distance)
        q.append((start[0], start[1], 0, 0))
        seen[0].add((start[0], start[1]))
        
        while q:
            row, col, keys, distance = q.popleft()
            if keys.bit_count() == k:
                return distance 
            
            for idx in range(len(directions)-1):
                new_row = row + directions[idx]
                new_col = col + directions[idx+1]
                
                if inbound(new_row, new_col) and (new_row, new_col) not in seen[keys] and grid[new_row][new_col] != '#':
                    curr = grid[new_row][new_col]
                    curr_keys = keys
                    # if it's a key
                    if curr.islower():
                        curr_keys = keys | (1 << (ord(curr) - ord('a')))
                    
                    # if it's a lock
                    if curr.isupper():
                        # if the key isn't found yet
                        if curr_keys & (1 << (ord(curr) - ord('A'))) == 0:
                            seen[keys].add((new_row, new_col))
                            continue
                    
                    q.append((new_row, new_col, curr_keys, distance+1))
                    seen[curr_keys].add((new_row, new_col))
                    
                    
        return -1
                            
                        
                        
                        
                    
            
            
            
                
            
            