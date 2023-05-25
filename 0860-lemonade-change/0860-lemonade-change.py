class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        counter = defaultdict(int)
        
        for b in bills:
            if b == 5:
                counter[b] += 1
            elif b == 10:
                if not counter[5]:
                    return False
                counter[5] -= 1
                counter[10] += 1
            elif b == 20:
                if counter[5] < 3 and (not counter[10] or not counter[5]):
                    return False
                if counter[10] > 0 and counter[5]:
                    counter[10] -= 1
                    counter[5] -= 1
                else:
                    counter[5] -= 3
                    
                counter[20] += 1
                
        return True
                
                
        
        