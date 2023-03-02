class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        index_freq = [0] * (len(nums) + 1)
        max_sum = 0
        
        for start, end in requests:
            index_freq[start] += 1
            index_freq[end+1] -= 1
            
        #index_freq sum
        for idx in range(1, len(index_freq)):
            index_freq[idx] += index_freq[idx-1]
                    
        index_freq.sort(reverse=True)
        nums.sort(reverse=True)
        
        for idx in range(len(nums)):
            max_sum += index_freq[idx] * nums[idx]
            
        return max_sum % (10**9 + 7)
            
            
            