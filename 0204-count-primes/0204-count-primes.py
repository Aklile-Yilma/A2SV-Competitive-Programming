class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n == 0 or n == 1:
            return 0
        
        is_prime = [True for _ in range(n+1)]
        print
        is_prime[0], is_prime[1] = False, False
        
        count = 0
        
        d = 2
        while d < n:
            if is_prime[d]:
                count += 1
                j = 2 * d
                while j <= n:
                    is_prime[j] = False
                    j += d
            d += 1
                
        return count