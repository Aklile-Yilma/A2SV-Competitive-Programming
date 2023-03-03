class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def helper(start, end):
            
            if start > end:
                return 
            
            s[start], s[end] = s[end], s[start]
            return helper(start+1, end-1)
        
        return helper(0, len(s)-1)
                
            