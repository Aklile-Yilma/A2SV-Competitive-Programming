class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # base case: when n == 1 that means that 3^0 exists
        if n == 1:
            return True
        # if the current n is less than 3 that means it doesn't have any x such that 3^x = n   
        
        if n < 1:
            return False
        
        return self.isPowerOfThree(n/3)