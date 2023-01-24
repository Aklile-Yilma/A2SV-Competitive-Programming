class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq_arr= [0]*3
        
        for value in nums:
            freq_arr[value]+=1
                        
        freq_idx=0
        for idx in range(len(nums)):  
            # move the pointer as long as we have no count value in the freq array
            while freq_arr[freq_idx]== 0:
                freq_idx+=1
            nums[idx]= freq_idx
            freq_arr[freq_idx]-=1
                