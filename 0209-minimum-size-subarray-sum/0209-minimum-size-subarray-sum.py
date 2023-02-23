class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        #float('inf') used to make result infinetly large value for comparision of minimum
        
        left, result, total = 0, float('inf') , 0
        
        for right, value in enumerate(nums):
            
            total += value

                        
            while(total >= target):

                # keep track of the minimum length of contiguous subarray
                result = min(result , right - left + 1)
                # substract and move left pointer                  
                total -= nums[left]
                left += 1 
                

        # return zero if there is no window that can satisfy our condition               
        return 0 if result == float('inf') else result
            
        