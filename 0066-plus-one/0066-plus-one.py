class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[-1] != 9:
            digits[-1] += 1
            
            return digits
            
        right = len(digits) - 1
        while right >= 0 and digits[right] == 9:
            digits[right] = 0
            right -= 1     
            
        if right == -1:
            digits.insert(0, digits[0] + 1)
        else:
            digits[right] += 1
            
        return digits