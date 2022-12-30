class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        
        num = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        
        result1 = 0
        result2 = 0
        

        for char in num1:
            # recreate the number from base0 
            result1 = (10*result1) + num[char]
                        
        for char in num2:
            result2 = (10*result2) + num[char]
            
            
        return str(result1 * result2)
            
            
        
