class Solution:
    def jump(self, nums: List[int]) -> int:
        
        N = len(nums)
        start = end = num_jumps = 0
        
        while end < N - 1:
            num_jumps += 1
            max_end = end + 1
            
            for i in range(start, end + 1):
                if nums[i] + i >= N - 1:
                    return num_jumps
                
                max_end = max(max_end, nums[i] + i)
            
            start = end
            end = max_end
        
        return num_jumps
            