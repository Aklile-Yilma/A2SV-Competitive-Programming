class Solution:
    def mySqrt(self, x: int) -> int:
        
        low = 0
        # we know for sure the square root won't be bigger than x//2
        high = (x // 2) + 1
        
        
        while low <= high:
            mid = (low + high) // 2
            
            if mid*mid < x:
                low = mid + 1
            elif mid*mid > x:
                high = mid - 1
            else:
                return mid
            
        return high
            
        