class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq_arr=[0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i]>nums[j]):
                    freq_arr[i]+=1
        return freq_arr
    
    
    
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         nums_sort = sorted(nums)
#         length = len(nums)
#         answer = []
#         for i in range(length):
# #finding the index of the items of the unsorted list(nums) , in the sorted list(nums_sort)     
#             idx = nums_sort.index(nums[i])
#             print(idx)
#             answer.append(idx)
#         return answer
