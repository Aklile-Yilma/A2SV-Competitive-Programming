class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        n = len(arr)
        left = self.countLeftSmaller(arr)
        right = self.countRightSmaller(arr)
        total = 0
        
        for idx in range(n):
            total += arr[idx] * left[idx] * right[idx]
            
        return total % (10**9 + 7)
        
        
    def countRightSmaller(self, arr: List[int]):
        n = len(arr)
        right = [1] * n
        stack = [(arr[-1], 1)]
        
        for i in range(n-2, -1, -1):
            while stack and stack[-1][0] > arr[i]:
                right[i] += stack.pop()[1]
            
            stack.append((arr[i], right[i]))
            
        return right
    
    def countLeftSmaller(self, arr: List[int]):
        n = len(arr)
        left = [1] * n
        stack = [(arr[0], 1)]
        
        for i in range(1, n):
            while stack and stack[-1][0] >= arr[i]:
                left[i] += stack.pop()[1]
                
            stack.append((arr[i], left[i]))
            
        return left
        

        