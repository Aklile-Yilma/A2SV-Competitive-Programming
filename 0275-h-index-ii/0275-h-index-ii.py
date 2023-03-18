class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        size = len(citations)
        low = 0
        high = len(citations) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if citations[mid] >= size - mid:
                high = mid - 1
            else:
                low = mid + 1
                
        return size - low if low < size and citations[low] != 0 else 0
                
                
                