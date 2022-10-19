from typing import *
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures)
        stack = []
        
        for today_day, today_temp in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < today_temp:
                
                past_day = stack.pop()
                answer[past_day] = today_day - past_day
                
            stack.append(today_day)
            
        return answer


s= Solution()
s.dailyTemperatures([73,74,75,71,69,72,76,73])