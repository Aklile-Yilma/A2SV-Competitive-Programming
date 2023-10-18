class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return len(nums)
        
        prev_difference = nums[1] - nums[0]
        count = 2 if prev_difference != 0 else 1
        
        for i in range(2, len(nums)):
            current_difference = nums[i] - nums[i-1]
            if (current_difference > 0 and prev_difference <= 0) or (current_difference < 0 and prev_difference >= 0):
                count += 1
                prev_difference = current_difference
                
        return count