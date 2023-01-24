class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        holder = 0
        
        for seeker in range(len(nums)):
            
            if nums[seeker] != 0:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
                
        return nums
            

# two pointer solution
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:            

#         #zero_pointer to keep track of where the zero element is
#         zero = 0
#         #end pointer points at the end of the array 
#         end = len(nums) - 1
        
        
        
#         while zero < end:
#             if nums[zero] == 0:
#                 nums += [nums.pop(zero)]
#                 # moving the end pointer to left because zero has been inserted
#                 end -=1
#             else: 
#                 #moving the zero pointer because the current number is not zero
#                 zero +=1
                
#         return nums
        
        
