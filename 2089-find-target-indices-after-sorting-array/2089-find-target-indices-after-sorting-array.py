class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums= sorted(nums)
        
        indices = []
        for idx in range(len(nums)):
            if(target==nums[idx]):
                indices.append(idx)
                
        return indices