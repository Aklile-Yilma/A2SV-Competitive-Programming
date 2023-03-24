class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        res = []
        #cyclic sort
        for ptr in range(len(nums)):
            while nums[ptr] != ptr + 1:
                correct_pos = nums[ptr] - 1
                if nums[ptr] == nums[correct_pos]:
                    break
                    
                nums[ptr], nums[correct_pos] = nums[correct_pos], nums[ptr] 
                
                
        for idx in range(len(nums)):
            if nums[idx] != idx + 1:
                res.append(idx + 1)
            
        return res