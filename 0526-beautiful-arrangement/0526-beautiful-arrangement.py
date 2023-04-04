class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        
        def backtrack(currPermLen, num, start):
            nonlocal count
            if currPermLen == n:
                count += 1
                return
            
            for idx in range(n):
                curr_element = idx + 1
                if (curr_element % (start+1) != 0 and (start + 1) % curr_element != 0):
                    continue
                
                is_visited = num & (1 << idx)
                if not is_visited: 
                    #place candidate
                    currPermLen += 1

                    #backtrack
                    backtrack(currPermLen,  num | (1 << idx), start+1)
                    
                    #remove candidate
                    currPermLen -= 1
                    # num = num ^ (1 << idx)
                    
            return
        
        backtrack(0, 0, 0)
        
        return count
        
        