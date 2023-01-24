class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        # since the array is sorted we can use colliding two pointer to get the indices
        
        while left < right:
            
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            
            elif numbers[left] + numbers[right] < target:
                left += 1
                
            else:
                right -= 1
                
                
                
        