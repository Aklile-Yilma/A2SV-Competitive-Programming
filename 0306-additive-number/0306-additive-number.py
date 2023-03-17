class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def checkleadingzero(start, end):
            curr = num[start:end + 1]
            if  curr != str(int(curr)):
                return True
            
            return False
            
        
        def backtrack(start, first, second):
            
            if start >= len(num):
                return True
            
            
            for idx in range(start, len(num)+1):
                val = int(num[start:idx+1])
                
                if checkleadingzero(start, idx):
                    continue
                    
                #prune
                if first + second == val:
                    if backtrack(idx + 1, second, val):
                        return True
                    
            return False
        
        
        for first_idx in range(len(num)-2):
            if checkleadingzero(0, first_idx):
                continue
                
            first = int(num[:first_idx+1])
                
            for second_idx in range(first_idx+1, len(num)-1, 1):
                
                if checkleadingzero(first_idx+1, second_idx):
                    break
                
                second = int(num[first_idx+1:second_idx+1])
                
                if backtrack(second_idx + 1, first, second):
                    return True
                
        return False
                
                    