class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greater = -1
        for idx in range(len(arr)-1, -1, -1):
            
            greater,arr[idx] = arr[idx], greater    
            if greater < arr[idx]:
                greater = arr[idx]
                
        return arr
                