class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        self.count = [0] * len(nums)        
        
        self.nums = list(zip(nums, range(len(nums))))
        self.merge_sort(0, len(nums)-1, self.nums)

        return self.count
        
    def count_valid(self, left_half, left, right_half):

        count = 0
        right = len(right_half) - 1

        for left in range(len(left_half)-1, -1, -1):
            while right >= 0 and left_half[left] <= right_half[right]:
                right -= 1
            
            count = right + 1
            idx = left_half[left][1]
            self.count[idx] += count 

        return count
        
    def merge_sort(self, left, right, arr):

        if left == right:
            return [arr[left]]
        
        
        mid = left + (right - left) // 2
        left_half = self.merge_sort(left, mid, arr)
        right_half = self.merge_sort(mid+1, right, arr)
        
        #count before merging the two sorted arrays
        self.count_valid(left_half, mid, right_half)

        return self.merge(left_half, right_half)
    
    
    def merge(self, arr1, arr2):

        arr1_ptr, arr2_ptr = 0, 0
        arr3 = []
        
        while arr1_ptr < len(arr1) and arr2_ptr < len(arr2):
            
            if arr1[arr1_ptr] <= arr2[arr2_ptr]:
                arr3.append(arr1[arr1_ptr])
                arr1_ptr += 1
            else:
                arr3.append(arr2[arr2_ptr])
                arr2_ptr += 1
                
        arr3.extend(arr1[arr1_ptr:])
        arr3.extend(arr2[arr2_ptr:])
        
        return arr3
    
    