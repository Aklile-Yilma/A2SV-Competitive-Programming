class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        distance = float('inf')
        idx_in_list = -1

        for idx ,coordinate in enumerate(points):
            if(coordinate[0] == x or coordinate[1] == y):
                
                # calculate manhattan distance
                curr_distance = abs(coordinate[0]- x) + abs(coordinate[1] - y)
                # update idx in list if it's valid minimum distance
                if(curr_distance < distance):
                    idx_in_list = idx
                # keep track of min distance
                distance = min(distance, curr_distance)
                
                
        return idx_in_list 
                