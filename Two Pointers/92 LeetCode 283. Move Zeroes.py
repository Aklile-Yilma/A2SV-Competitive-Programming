class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #zero_pointer to keep track of where the zero element is
        zero = 0
        #end pointer points at the end of the array 
        end = len(nums) - 1
        

        
        while zero < end:
            if nums[zero] == 0:
                nums += [nums.pop(zero)]
                # moving the end pointer to left because zero has been inserted
                end -=1
            else: 
                #moving the zero pointer because the current number is not zero
                zero +=1
                
        return nums
        