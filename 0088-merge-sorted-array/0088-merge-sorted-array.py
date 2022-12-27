class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

#         idx2 = 0
#         for idx in range(m, len(nums1), 1):
#             if(idx2 < n):
#                 nums1[idx] = nums2[idx2]
#                 idx2 +=1

#         nums1ptr=0
#         nums2ptr=m
        
#         while(nums2ptr<len(nums1)):
#             if nums1[nums1ptr] > nums1[nums2ptr]:
#                 nums1[nums1ptr],nums[nums[]]





        # nums1.sort()

        # idx = 0 
        # for num1, num2 in zip(nums1, nums2):
        #     if(num2 > num1):
        #         nums1.insert(idx, num2)
        # idx2 = n-1
        # last=n+m-1
        # for idx in range(m, 0, -1):
        #     if nums1[idx] < nums2[idx2]:
        #         nums1[last]=nums2[idx2]
        #         last-=1
        #     else:
        #         n
        
        idx2 = 0
        for idx in range(m, len(nums1), 1):
            if(idx2 < n):
                nums1[idx] = nums2[idx2]
                idx2 +=1

        nums1.sort()
            




