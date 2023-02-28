class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        #prefix 
        prefix = { 0: 1}
        odd_sums = 0
        count = 0
        
        for num in nums:
            if num%2 != 0:
                odd_sums += 1
            
            diff = odd_sums - k
            count += prefix.get(diff, 0)
            prefix[odd_sums] = prefix.get(odd_sums, 0) + 1
            
        return count
                
            
                