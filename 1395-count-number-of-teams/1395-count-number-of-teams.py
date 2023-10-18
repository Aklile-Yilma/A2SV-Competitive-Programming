class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        n = len(rating)
        smaller_map = {}
        
        def countSmaller(arr):
            n = len(arr)
            
            for i in range(n):
                count = 0
                for j in range(i):
                    if arr[j] < arr[i]:
                        count += 1        
                smaller_map[i] = count
                
            ans = 0
            for i in range(n):
                for j in range(i):
                    if arr[j] < arr[i]:
                        ans += smaller_map[j]
                        
            return ans
                
        return countSmaller(rating) + countSmaller(rating[::-1])
        
                        