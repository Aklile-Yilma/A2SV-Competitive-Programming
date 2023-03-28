class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        self.count = 0
                
        self.merge_sort(0, len(nums)-1, nums)
        
        return self.count
            
        
    def count_valid(self, left_half, right_half):

        count = 0
        right = len(right_half) - 1      

        for left in range(len(left_half)-1, -1, -1):
            while right >= 0 and left_half[left] <= right_half[right] * 2:
                right -= 1
            
            count += right + 1            

        return count

    def merge_sort(self, left, right, arr):

        if left == right:
            return [arr[left]]

        mid = left + (right - left) // 2
        left_half = self.merge_sort(left, mid, arr)
        right_half = self.merge_sort(mid + 1, right, arr)

        #count for ai >  2 * aj
        self.count += self.count_valid(left_half, right_half)

        return self.merge(left_half, right_half)
        
        
    def merge(self, arr1, arr2):

        arr1_pointer = 0
        arr2_pointer = 0
        arr3 = []
        idx = 0

        while arr1_pointer < len(arr1) and arr2_pointer < len(arr2):
            if arr1[arr1_pointer] <= arr2[arr2_pointer]:
                arr3.append(arr1[arr1_pointer])
                arr1_pointer += 1
            else:
                arr3.append(arr2[arr2_pointer])
                arr2_pointer += 1
            idx += 1

        arr3 += arr1[arr1_pointer:]
        arr3 += arr2[arr2_pointer:]

        return arr3
        
        