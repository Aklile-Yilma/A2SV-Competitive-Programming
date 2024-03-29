class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        
        idx = 0
        largest_perimeter = 0
        
        while(idx < len(nums)):
            
            # a triangle is said to be formed if the sum two less length sides is greater than the third bigger side 
            if((idx+2) < len(nums) and (nums[idx] + nums[idx+1] > nums[idx+2])):
                curr_perimeter = nums[idx] + nums[idx+1] + nums[idx+2]
                largest_perimeter = max(largest_perimeter, curr_perimeter)
                
            idx+=1
                    
                
        return largest_perimeter
            
                
            
            
        
        
        