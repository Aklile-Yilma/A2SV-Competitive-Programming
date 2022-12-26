class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        distance = float('inf')
        idx_in_list = -1

        for idx ,coordinate in enumerate(points):
            if(coordinate[0] == x or coordinate[1] == y):
                curr_distance = abs(coordinate[0]- x) + abs(coordinate[1] - y)
                if(curr_distance < distance):
                    idx_in_list = idx
                distance = min(distance, curr_distance)
                
                
        return idx_in_list if distance != float('inf') else -1
                