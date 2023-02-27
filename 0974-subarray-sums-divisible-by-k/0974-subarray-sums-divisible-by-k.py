class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        running_sum = 0
        count = 0
        # {prefix: count}
        prefix_map = {0: 1}
        
        for num in nums:
            running_sum += num
            remainder = running_sum % k
            
            #count prefix that can be deducted to make our curr prefix divisible
            count += prefix_map.get(remainder, 0)
            #add prefix
            prefix_map[remainder] = prefix_map.get(remainder, 0) + 1
            
            
        return count
            
        
        
        
        