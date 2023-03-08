class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        peak_idx = -1
        
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] >= arr[mid + 1]:
                high = mid - 1
            
            if mid != 0 and arr[mid] >= arr[mid - 1]:
                low = mid + 1
            
            if mid == 0:
                break                
                
        peak_idx = mid if mid != 0 else (mid + 1)
        
        return peak_idx
                
                