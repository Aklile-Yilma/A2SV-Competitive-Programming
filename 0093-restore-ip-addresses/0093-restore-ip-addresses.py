class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        answer = []
        
        def backtrack(start, curr):
            
            if start >= len(s):
                if len(curr) == 4:
                    answer.append('.'.join(curr.copy()))
                return
            
            if len(curr) >= 4:
                return
            
            for idx in range(start, len(s)):
                substring = s[start:idx+1]
                
                if not self.validate(substring):
                    continue
                curr.append(substring)
                backtrack(idx + 1, curr)
                curr.pop()
                
            return
            
    
        for idx in range(len(s)):
            substring = s[:idx+1]
            if not self.validate(substring):
                continue
            backtrack(idx+1, [substring])
            
        return answer
            
            
            
            
    def validate(self, substring):
        
        if len(substring) > 1 and substring[0] == '0':
            return False
        
        if int(substring) > 255:
            return False
        
        return True