class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        # formula (n) + (n+1) + (n+2) = num
        # 3n + 3 = num
        
        start = (num - 3) // 3
        
        if num%3 == 0:
            return [start, start+1, start+2]
            
        else:
            return []
        
        