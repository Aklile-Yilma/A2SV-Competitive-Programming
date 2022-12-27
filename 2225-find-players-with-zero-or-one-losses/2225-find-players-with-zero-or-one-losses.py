class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        # count the number of times a player loses
        count = {}
        winners = []
        lost_one_match = []
        
        
        for match in matches:
            
            player1 = match[0]
            player2 = match[1]
            
            if(player1 not in count.keys()):
                count[player1] = 0
            
                
            if(player2 not in count.keys()):
                count[player2] = 1
            else:
                count[player2] += 1     
                
        for player in count.keys():
            if(count[player] == 0):
                winners.append(player)
            elif(count[player] == 1):
                lost_one_match.append(player)
                
        
        winners.sort()
        lost_one_match.sort()
        
        return [winners, lost_one_match]
        
        