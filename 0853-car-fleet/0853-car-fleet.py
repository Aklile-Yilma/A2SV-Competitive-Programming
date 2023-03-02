class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos_speed = [(pos, speed) for pos, speed in zip(position, speed)]
        #sort by position
        pos_speed.sort(reverse=True)
        num_fleet = 0
        # monotonic decreasing stack
        stack = []
        
        for pos, speed in pos_speed:
            
            time_left = (target - pos)/speed
            
            while stack and stack[-1] < time_left:
                stack.pop()
            
            if not stack:
                num_fleet += 1
            
            stack.append(time_left)
            
        return num_fleet
            
        
        
        