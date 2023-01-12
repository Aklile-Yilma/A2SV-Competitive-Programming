class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        
        for idx, num in enumerate(nums):
            
            if idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                nums[idx] *= 2
                nums[idx+1] = 0
                
        
        end = len(nums)-1
        zero = 0
        
        while zero < end:
            if nums[zero] == 0:
                nums += [nums.pop(zero)]
                # moving the end pointer to left because zero has been inserted
                end -=1
            else: 
                #moving the zero pointer because the current number is not zero
                zero +=1
                
        return nums