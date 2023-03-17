class Solution:
        
    def __init__(self):
        self.result = 0
        self.valid_queen_pos  = set()
        self.ans = []
        self.board = []
    
    def solveNQueens(self, n):

        self.backtrack(1, n, [])
        self.generateBoard(self.ans, n)
        
        return self.board

    def backtrack(self, row, n, curr_cand):
        #base case
        if row > n:
            if len(self.valid_queen_pos) == n:
                self.ans.append(curr_cand.copy())
                self.result += 1
            return 
        
        for col in range(1, n+1):
            #if current position is valid, choose that position (pick and move)
            if self.isValid((row, col), self.valid_queen_pos, n):

                self.valid_queen_pos.add((row, col))
                curr_cand.append([row, col])
                self.backtrack(row + 1, n, curr_cand)
                curr_cand.pop()
                self.valid_queen_pos.remove((row, col))
        
    
    def isValid(self, pos, valid_queen_pos, n):
        
        row, col = pos

        row_index = row
        #check if postion is valid vertically
        while row_index > 0:
            if (row_index, col) in valid_queen_pos:
                return False

            row_index -= 1

        
        row_index = row  
        diag_col = col
        #check if position is valid right diagnolally
        while row_index > 0 and diag_col <= n:
            if (row_index, diag_col) in valid_queen_pos:
                return False

            row_index -= 1
            diag_col += 1


        row_index = row  
        diag_col = col
        #check if position is valid left diagnolally
        while row_index > 0 and diag_col > 0:
            if (row_index, diag_col) in valid_queen_pos:
                return False

            row_index -= 1
            diag_col -= 1
        
        #otherwise return true
        return True

    def generateBoard(self, positions, n):
        
        for idx in range(len(positions)):
            board = positions[idx]
            curr_board = []
            for row, col in board:
                line = ["."] * n
                line[col-1] = "Q"
                curr_board.append("".join(line))
                
            self.board.append(curr_board)
            
        return
        
            
            
        
        
        
        
        