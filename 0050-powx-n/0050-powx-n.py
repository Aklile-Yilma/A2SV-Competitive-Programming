class Solution:
    def myPow(self, x: float, n: int) -> float:
            def helper(x, n):
                #base case: for x= 0 it will always be zero
                if x == 0: return 0

                #base case: when n reaches 0 then we can return recursion results from bottom up 
                if(n == 0): return 1
                
                #recursion call             
                curr_result = helper(x, n//2)
                
                #since we calculated only half of n we need to square it  
                curr_result = curr_result * curr_result
                
                # for odd exponent return x*curr
                return x * curr_result if n % 2 else curr_result

            result = helper(x, abs(n))
            
            # for negative exponents return 1/result
            return result if n > 0 else 1/result