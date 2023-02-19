class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if k == 0:
            return False
        
        k_map = {}
        left = 0
        
        for right in range(len(nums)):
            if left != right and nums[right] in k_map:
                return True
            
            if abs(right - left + 1) > k:
                del k_map[nums[left]] 
                left += 1
                
            k_map[nums[right]] = True
            
                
        return False