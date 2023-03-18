class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        prefix = defaultdict(int)
        prefix[0] = 1
        count = 0
        total = 0
        
        for num in nums:
            total += num
            count += prefix[(total - goal)]
            prefix[total] += 1
            
        return count
