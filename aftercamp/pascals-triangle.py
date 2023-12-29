class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        
        ans = []
        ans.append([1])
        ans.append([1, 1])
        
        def recursion(row):
            nonlocal ans
            if row == 1:
                return [1]
            if row == 2:
                return [1, 1]
            
            
            arr = [1] * row
            some_arr = recursion(row-1) 
            for i in range(1, row-1):
                arr[i] = some_arr[i-1] + some_arr[i]
            
            ans.append(arr)
            return arr
        
        recursion(numRows)
        return ans
        
        