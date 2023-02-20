class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nums.sort()
        
        left = 0
        for right in range(len(nums)):
            
            if right != left and nums[left] == nums[right]:
                return nums[left]
            
            if right - left + 1 > 1:
                left += 1
                
        
        