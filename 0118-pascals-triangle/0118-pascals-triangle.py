class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        answer = [[1]]
        def helper(row):
            nonlocal answer
            
            if row == 1:
                return [1]
            
            before = helper(row-1)
            
            new_arr = [1]
            
            for idx in range(len(before)-1):
                
                new_arr.append(before[idx] + before[idx+1])
                
            new_arr.append(1)
            
            answer.append(new_arr.copy())
            
            return new_arr
            
        helper(numRows)

        return answer