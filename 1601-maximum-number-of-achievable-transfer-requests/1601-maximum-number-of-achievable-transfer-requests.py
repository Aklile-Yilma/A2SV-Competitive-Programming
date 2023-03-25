class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        
        result =  0   
        buildings = [0] * n
        def backtrack(start, curr, buildings):
            nonlocal result
            
            if start >= len(requests):
                return
            
            for idx in range(start, len(requests)):
                #handle candidate
                curr.append(requests[idx])
                from_, to_ = requests[idx]
                buildings[from_] -= 1
                buildings[to_] += 1
                
                #check if net buildings movement is all zero
                if all(buildings[idx] == 0 for idx in range(len(buildings))):
                    result = max(result, len(curr))
                
                backtrack(idx + 1, curr, buildings)
                
                #handle remove candidate
                request = curr.pop()
                from_, to_ = request
                buildings[from_] += 1
                buildings[to_] -= 1
            
            return
        
        backtrack(0, [], buildings)
        
        return result