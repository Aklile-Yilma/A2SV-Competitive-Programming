class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[None for _ in range(n)] for _ in range(n)]
        
        #fill ones
        for i in range(n):
            dp[i][i] = True
            
        x, y = 0, 0
        #fill twos
        for i in range(n):
            if i + 1 < n:
                dp[i][i+1] = True if s[i] == s[i+1] else False
                if dp[i][i+1]:
                    x, y = (i, i+1)
        
        for k in range(2, n):
            for i in range(n-k):
                dp[i][i+k] = (s[i+k] == s[i]) and dp[i+1][i+k-1]
                if dp[i][i+k]:
                    x, y = (i, i+k)
                   
        return s[x:y+1]
        
                    