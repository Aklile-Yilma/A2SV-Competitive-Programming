class Solution:
    def minSteps(self, n: int) -> int:
        
        def primeFactorization(num):
            
            result = 0
            d = 2
            while num != 1:
                while num % d == 0:
                    result += d
                    num = num // d
                d += 1
                
            return result

        return primeFactorization(n)
        