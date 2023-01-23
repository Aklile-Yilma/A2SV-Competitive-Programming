class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
  
        peak = max(arr)
        peak_idx = arr.index(peak)
        
        if peak_idx == len(arr)-1:
            return False
        
        if peak_idx == 0:
            return False
        
        increasing_mountain = arr[:peak_idx+1]
              
        if len(set(increasing_mountain)) != len(increasing_mountain):
            return False
        
        decreasing_mountain = arr[peak_idx:]
        if len(set(decreasing_mountain)) != len(decreasing_mountain):
            return False
        
        
        if not sorted(increasing_mountain) == increasing_mountain:
            return False
        
        if not sorted(decreasing_mountain, reverse=True) == decreasing_mountain:
            return False
        
        return True
        
        