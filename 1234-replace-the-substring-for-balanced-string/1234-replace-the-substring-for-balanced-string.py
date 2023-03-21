class Solution:
    def balancedString(self, s: str) -> int:
        
        valid_count = len(s) // 4
        counter = Counter(s)
        
        if all(counter[ch] == valid_count for ch in counter):
            return 0
        
        
        left = 0
        res = float('inf')
        
        for right in range(len(s)):
            counter[s[right]] -= 1
            
            while left <= right and all(counter[ch] <= valid_count for ch in counter):
                res = min(res, right - left + 1)
                counter[s[left]] += 1
                left += 1
                
        return res
            
        
        
        