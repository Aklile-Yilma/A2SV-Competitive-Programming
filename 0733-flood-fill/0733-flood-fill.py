class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        initial_color = image[sr][sc]
        directions = [1, 0, -1, 0, 1]        
        inbound = lambda row, col: 0 <= row <  len(image) and 0 <= col < len(image[0])
        
        q = deque()
        if color != image[sr][sc]:
            q.append((sr, sc))
            
        while q:
            size = len(q)
            for idx in range(size):
                row, col = q.popleft()
                if not inbound(row, col) or image[row][col] != initial_color:
                    continue
                
                image[row][col] = color
                for idx in range(len(directions)-1):
                    q.append((row + directions[idx], col + directions[idx+1]))
                    
            
        return image
                