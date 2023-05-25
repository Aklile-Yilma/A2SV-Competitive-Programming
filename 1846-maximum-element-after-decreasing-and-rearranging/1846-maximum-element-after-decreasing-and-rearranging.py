class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        arr.sort()
        if arr[0] != 1:
            arr[0] = 1
            
        for idx in range(len(arr)-1):
            curr = arr[idx]
            nxt = arr[idx+1]
            if abs(nxt-curr) > 1:
                arr[idx+1] = curr+1
                
        return arr[-1]
                
                