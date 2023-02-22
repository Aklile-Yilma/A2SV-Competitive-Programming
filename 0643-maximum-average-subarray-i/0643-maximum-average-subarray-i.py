class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        curr_sum = 0
        left = 0
        
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            if right-left+1 == k:
                max_avg = max(max_avg, curr_sum/k)
                curr_sum -= nums[left]
                left += 1
        
        return max_avg