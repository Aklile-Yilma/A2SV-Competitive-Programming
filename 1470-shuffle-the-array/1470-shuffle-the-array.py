class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        left = 0
        right = n
        shuffle = []
        isLeft = True
        
        while right < len(nums):
            if isLeft:
                shuffle.append(nums[left])
                left += 1
                isLeft = False
            else:
                shuffle.append(nums[right])
                right += 1
                isLeft = True
                
        return shuffle
                
            
            