class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a%b)
        
        count = 0
        for ptr in range(len(nums)):
            prev_gcd = nums[ptr]
            for runner in range(ptr, len(nums)):
                curr_gcd = gcd(prev_gcd, nums[runner])
                
                if curr_gcd >= k:
                    if curr_gcd == k:
                        count += 1
                    prev_gcd = curr_gcd
                else:
                    break
        
        return count
                