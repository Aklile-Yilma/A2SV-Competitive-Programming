class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        car_trip = [0] * 1001

        for num_pass, from_i, to_i in trips:
            car_trip[from_i] += num_pass
            car_trip[to_i] -= num_pass

        #compute prefix sum
        for idx in range(1, len(car_trip)):
            car_trip[idx] += car_trip[idx-1]

        #check capacity
        for curr_pass in car_trip:
            if curr_pass > capacity:
                return False

        return True 

        
            
            