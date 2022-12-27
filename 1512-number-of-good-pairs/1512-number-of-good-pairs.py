class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        pairs = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                
                if(nums[i] == nums[j]):
                    pairs += 1
                    
        return pairs
                    