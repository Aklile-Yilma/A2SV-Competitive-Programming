class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        unfair = [float('inf')]
        buckets = [0] * k
        
        def backtrack(idx, unfair):
            if idx >= len(cookies):
                unfair[0] = min(unfair[0], max(buckets))
                return
            
            for i in range(k):
                buckets[i] += cookies[idx]
                if buckets[i] < unfair[0]:
                    backtrack(idx + 1, unfair)
                    
                buckets[i] -= cookies[idx]
        
        backtrack(0, unfair)
        
        return unfair[0]
        
        