class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players_ptr = 0
        trainers_ptr = 0
        max_match = 0
        
        players.sort()
        trainers.sort()
        
        while players_ptr < len(players) and trainers_ptr < len(trainers):
            
            if players[players_ptr] <= trainers[trainers_ptr]:
                max_match += 1
                players_ptr += 1
                trainers_ptr += 1
            else:
                trainers_ptr += 1
                
        return max_match
                
            
                
            
            
            
            