class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        result = 0
        
        def backtrack(start, curr_cand):
            nonlocal result
            if start >= len(arr):
                return
            
            for idx in range(start, len(arr)):
                curr_cand.append(arr[idx])
                
                curr_string = ''.join(curr_cand)
                
                if len(set(curr_string)) == len(curr_string):
                    result = max(result, len(curr_string))
                    backtrack(idx + 1, curr_cand)
                
                curr_cand.pop()
                
            return
        
        backtrack(0, [])
        
        return result