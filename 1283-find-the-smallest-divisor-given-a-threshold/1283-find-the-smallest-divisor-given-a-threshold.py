class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def isGreater(mid):
            #check if greater than treshold
            curr_sum = 0
            for num in nums:
                curr_sum += math.ceil(num/mid)
                
            if curr_sum > threshold:
                return True
            
            return False
        
        low = 1
        high = sum(nums)
        
        while low <= high:
            mid = (low + high) // 2
            
            if isGreater(mid):
                low = mid + 1
            else:
                high = mid - 1
                
                
        return low
        
        