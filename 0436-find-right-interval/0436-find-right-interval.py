class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        def isGreater(mid, curr_interval, intervals_index):
            
            end_i = curr_interval[1]
            start_j = intervals_index[mid][0][0]
            
            if start_j >= end_i:
                return True
            
            return False
            
            
        intervals_index = [(intervals[idx], idx) for idx in range(len(intervals))]
        
        intervals_index.sort()
        
        result = []
        
        for interval in intervals:
            
            low = 0
            high = len(intervals_index) - 1
            
            while low <= high:
                mid = (low + high) // 2
                
                if isGreater(mid, interval, intervals_index):
                    high = mid - 1
                else:
                    low = mid + 1
        
            idx = intervals_index[low][1] if 0 <= low < len(intervals) else -1
            result.append(idx)
        
        
        return result