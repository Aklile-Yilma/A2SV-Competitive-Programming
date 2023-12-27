class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #dict: key: set
        row = defaultdict(set)
        col = defaultdict(set)
        sec = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                item = board[r][c]
                if item == '.':
                    continue
                
                s = (r // 3, c // 3)
                if item in row[r] or item in col[c] or item in sec[s]:
                    return False
                else:
                    row[r].add(item)
                    col[c].add(item)
                    sec[s].add(item)

        return True