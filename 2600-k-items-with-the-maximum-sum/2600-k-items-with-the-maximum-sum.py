class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        arr = []
        def add(arr, size, num): 
            while size:
                arr.append(num)
                size -= 1
                
        add(arr, numOnes, 1)
        add(arr, numZeros, 0)
        add(arr, numNegOnes, -1)
        
        max_sum = 0
        for i in range(k):
            max_sum += arr[i]
            
        return max_sum
            
                
            
        
 
            
        