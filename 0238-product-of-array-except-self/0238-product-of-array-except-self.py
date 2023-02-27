class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        prefix = [1] * size
        suffix = [1] * size
        answer = [1] * size
        
        for idx in range(1, size):
            prefix[idx] *= prefix[idx-1] * nums[idx-1]
        
        for idx in range(size-2, -1, -1):
            suffix[idx] *= suffix[idx+1] * nums[idx+1]
         
        for idx in range(size):
            answer[idx] = prefix[idx] * suffix[idx]
            
        return answer
        
            
        