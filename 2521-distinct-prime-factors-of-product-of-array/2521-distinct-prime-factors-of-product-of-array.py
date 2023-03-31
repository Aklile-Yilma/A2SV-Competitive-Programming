class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        factors = set()
        
        def prime_factorization(num):
            d = 2
            
            while d * d <= num:
                while num % d == 0:
                    factors.add(d)
                    num = num // d
                d += 1
                
            if num > 1:
                factors.add(num)
            
            return factors
                
        for idx in range(len(nums)):
            prime_factorization(nums[idx])    
                        
        
        return len(factors)