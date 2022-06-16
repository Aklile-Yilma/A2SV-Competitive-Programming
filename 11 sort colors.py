class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.'
        '"""
        
        #Using counting sort
        freq_arr= [0]*3
        
        for value in nums:
            freq_arr[value]+=1
            
        j=0
        for i in range(len(nums)):  
            while (freq_arr[j]== 0):
                j+=1
            nums[i]= j
            freq_arr[j]-=1
                