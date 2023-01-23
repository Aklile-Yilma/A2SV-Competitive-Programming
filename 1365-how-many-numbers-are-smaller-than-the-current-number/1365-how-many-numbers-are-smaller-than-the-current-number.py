class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        freq_arr=[0]*len(nums)
        
        for idx1 in range(len(nums)):
            for idx2 in range(len(nums)):
                if(nums[idx1]>nums[idx2]):
                    freq_arr[idx1]+=1
        return freq_arr
    