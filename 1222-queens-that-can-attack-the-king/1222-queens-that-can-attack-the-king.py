class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = set((xq, yq) for xq, yq in queens)
        res = deque()
		
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        for dx, dy in directions:
            x, y = king
            while 0 <= x < 8 and 0 <= y < 8:
                x += dx
                y += dy
                if (x, y) in queens:
                    res.append([x, y])
                    break
        
        return res
            
        
        