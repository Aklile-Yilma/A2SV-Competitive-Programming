class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        sums = 0
        d = dict()
        # {prefix_sum : count}
        d[0] = 1
        
        for num in nums:
            sums += num
            diff = sums - k
            
            count += d.get(diff, 0)
            d[sums] = d.get(sums, 0) + 1
        
        return count
                
        
        
        
        