from typing import *

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left , right = 0, len(height) - 1   
        max_area = 0
        
        while left < right:
            
            area = min(height[left], height[right]) * (right - left)
            max_area = max(area, max_area)
          
             # Keep the higher point, move the smaller one as to try to get the highest combination
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
                    
                    
        return max_area
                
                
                
        
        
        
                
                
                
        
s= Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
