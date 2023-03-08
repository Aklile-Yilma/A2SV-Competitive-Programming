class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums or target not in nums:
            return [-1, -1]
        
        def findFirst(nums, target):
            low = 0
            high = len(nums) - 1
            
            while low <= high:
                mid = (low + high) // 2
                
                if nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            
            return low
        
        def findLast(nums, target):
            low = 0
            high = len(nums) - 1
            
            while low <= high:
                mid = (low + high) // 2
                
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
                    
            return high
                
        
        first_idx = findFirst(nums, target) 
        last_idx = findLast(nums, target)
        
        return [first_idx, last_idx]
        