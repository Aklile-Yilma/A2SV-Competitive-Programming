class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        
        for key in count:
            if count[key] == 1:
                return key
            
        