class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        LPS = self.buildLPS(needle)
        
        i, j = 0, 0
        n, m = len(haystack), len(needle)
        
        if m > n:
            return -1
        
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = LPS[j-1]
                    
            if j == m:
                return i - j
            
        return -1
        
    def buildLPS(self, pattern):
        
        prev = 0
        i = 1
        m = len(pattern)
        LPS = [0] * m
        
        while i < m:
            if pattern[i] == pattern[prev]:
                LPS[i] = 1 + prev
                prev += 1
                i += 1
            else:
                if prev == 0:
                    i += 1
                else:
                    prev = LPS[prev - 1]
                    
        return LPS
                

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
        
#         m = len(needle)
#         n = len(haystack)

#         if m > n:
#             return -1

#         alpha = 27
#         #calc for m
#         hash_m = 0
#         for idx in range(m):
#             hash_m += pow(alpha, m-1-idx) * (ord(needle[idx]) - 96)

#         #sliding window

#         left = 0 
#         hash_n = 0
#         for idx in range(m):
#             hash_n += pow(alpha, m-1-idx) * (ord(haystack[idx]) - 96)
        
#         if hash_n == hash_m:
#             return 0

#         left = 0 
#         for right in range(m, n):
#             # add last
#             add = (pow(alpha, 0) * (ord(haystack[right]) - 96))
#             # remove first
#             remove = (pow(alpha, m-1) * (ord(haystack[left]) - 96))
#             left += 1
#             hash_n = (hash_n  - remove) * alpha + add
            
#             if hash_n == hash_m:
#                 return left

#         return -1



            


