class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        res = []
        #cyclic sort
        for ptr in range(len(nums)):
            while nums[ptr] != ptr + 1:
                correct_pos = nums[ptr] - 1
                if nums[ptr] == nums[correct_pos]:
                    return nums[ptr]
                    
                nums[ptr], nums[correct_pos] = nums[correct_pos], nums[ptr] 
                
        return
            
        
        