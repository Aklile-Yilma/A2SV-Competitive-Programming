class Solution:        
    def validTicTacToe(self, board):
        def win(s): # return True if the player who use s wins
            #check vertical wins
            if board[0][0]==s and board[0][1]==s and board[0][2]==s: return True
            if board[1][0]==s and board[1][1]==s and board[1][2]==s: return True
            if board[2][0]==s and board[2][1]==s and board[2][2]==s: return True
            #check horizontal wins
            if board[0][0]==s and board[1][0]==s and board[2][0]==s: return True
            if board[0][1]==s and board[1][1]==s and board[2][1]==s: return True
            if board[0][2]==s and board[1][2]==s and board[2][2]==s: return True
            #check diagonal wins
            if board[0][0]==s and board[1][1]==s and board[2][2]==s: return True
            if board[0][2]==s and board[1][1]==s and board[2][0]==s: return True
            return False
        
        xNum, oNum = 0, 0
        for row in board:
            xNum+=row.count('X')
            oNum+=row.count('O')
            
        if oNum>xNum or xNum-oNum>=2: # "X" should always >= O, but only by 1 
            return False
        
        if xNum>=3:
            if xNum==oNum and win('X'): # put another "O" after "X" player winning
                return False
            if xNum!=oNum and win('O'): # put another "X" after "O" player winning
                return False
        return True

        