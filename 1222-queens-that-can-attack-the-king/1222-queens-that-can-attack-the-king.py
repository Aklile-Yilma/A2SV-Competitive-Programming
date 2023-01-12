class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = set((xq, yq) for xq, yq in queens)
        res = []
		# up, down right, left, diagonal down_left, diagonal up_right, diagonal down_right, diagonal up_left 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        for dx, dy in directions:
            # move in all 8 directions from the king
            x, y = king
            while 0 <= x < 8 and 0 <= y < 8:
                x += dx
                y += dy
                # break to get the most nearest queen in that row
                if (x, y) in queens:
                    res.append([x, y])
                    break
        
        return res
            
        
        