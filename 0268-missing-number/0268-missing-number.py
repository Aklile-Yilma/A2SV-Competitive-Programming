class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # to get range of number from 0  to n
        
        nums.append(None)
        
        for ptr in range(len(nums)):
            
            while nums[ptr] != ptr and nums[ptr] != None:
                
                right = nums[ptr]
                nums[ptr], nums[right] = nums[right], nums[ptr]
                
            
        for idx in range(len(nums)):
            if nums[idx] == None:
                return idx
            
        return -1
                