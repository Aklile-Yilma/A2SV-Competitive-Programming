class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        k = len(nums) - k 
        
        def quick_sort(arr, start, end):
            
            if end - start + 1 <= 1:
                return arr[start]
            
            pivot = arr[start]
            pivot_idx = start
            
            left = start
            
            for right in range(start, end+1):
                
                if arr[right] <= pivot:
                    arr[right], arr[left] = arr[left], arr[right]
                    left += 1
                    
            
            left -= 1
            arr[left], arr[pivot_idx] = arr[pivot_idx], arr[left]
            
            if k < left:
                return quick_sort(arr, start, left - 1)
            elif k > left:
                return quick_sort(arr, left + 1, end)
            else: 
                return arr[left]
                    
        return quick_sort(nums, 0, len(nums)-1)
        
        