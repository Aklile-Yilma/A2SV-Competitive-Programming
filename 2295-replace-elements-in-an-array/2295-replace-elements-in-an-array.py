class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        nums_map = {}
        for idx, num in enumerate(nums):
            nums_map[num] = idx
                    
        for num, replacement in operations:
            idx = nums_map[num]
            #remove the (key,value) pairs b/c they are no longer in the dict
            del nums_map[num]
            #replace the num in nums
            nums[idx] = replacement
            #update the dict
            nums_map[replacement] = idx
            
        return nums
            
            
            
        