class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        #decreasing monostack
        stack = [] #(num, cur_min)
        cur_min = float('inf')
        
        for num in nums:
            while stack and stack[-1][0] <= num:
                stack.pop()
            
            if stack and stack[-1][1] < num:
                return True
                            
            stack.append([num, cur_min])
            cur_min = min(cur_min, num)
        
        return False
        
                
            
        