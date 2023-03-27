class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        #merge the arrays into one array
        nums3 = []
        self.count = 0
        self.diff = diff
        
        for idx in range(len(nums1)):
            nums3.append(nums1[idx] - nums2[idx])
            
            
        self.merge_sort(0, len(nums3)-1, nums3)
        
        
        return self.count
            
        
    def count_valid(self, left_half, right_half):

        count = 0
        right = 0          
        for left in range(len(left_half)):

            while right < len(right_half) and left_half[left] - self.diff  > right_half[right]:
                right += 1

            count += len(right_half) - right 

        return count

    def merge_sort(self, left, right, arr):

        if left == right:
            return [arr[left]]

        mid = left + (right - left) // 2
        left_half = self.merge_sort(left, mid, arr)
        right_half = self.merge_sort(mid + 1, right, arr)


        return self.merge(left_half, right_half)
        
        
    def merge(self, arr1, arr2):
        #count for ai - diff <= aj
        self.count += self.count_valid(arr1, arr2)
        print(self.count)

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
            
            
