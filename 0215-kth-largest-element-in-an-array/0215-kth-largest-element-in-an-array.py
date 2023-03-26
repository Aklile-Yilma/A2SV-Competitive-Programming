class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quick_sort(arr, start, end):
            
            if end - start + 1 <= 1:
                return arr
            
            pivot = arr[start]
            pivot_idx = start
            
            left = start
            
            for right in range(start, end+1):
                
                if arr[right] <= pivot:
                    arr[right], arr[left] = arr[left], arr[right]
                    left += 1
                    
            
            left -= 1
            arr[left], arr[pivot_idx] = arr[pivot_idx], arr[left]
            
            quick_sort(arr, start, left - 1)
            quick_sort(arr, left + 1, end)
            
            return arr
        
        quick_sort(nums, 0, len(nums)-1)
        
        return nums[len(nums)-k]