class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        primes = []
        result = [0, float('inf')]
        def prime_sieve(n: int) -> list[bool]:
            is_prime: list[bool] = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False

            i = 2
            while i * i <= n:
                if is_prime[i]:
                    j = i * i
                    while j <= n:
                        is_prime[j] = False
                        j += i
                i += 1

            return is_prime

        
        all_primes = prime_sieve(right)
        prev = float('inf')
        diff = float('inf')
        for num in range(left, right+1):
            curr = num
            if all_primes[num]:
                if prev != float('inf') and curr - prev < result[1] - result[0]:
                    result = [prev, curr]
                    diff = curr - prev
                prev = curr
                
            if diff <= 2:
                break
        
        return result if result != [0, float('inf')] else [-1, -1]
    
        