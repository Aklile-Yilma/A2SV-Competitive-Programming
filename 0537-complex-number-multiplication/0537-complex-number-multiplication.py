class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        # formula
        # (a + ib) (c + id) = (ac - bd) + i(ad + bc).
    
        real1, imaginary1 = map(int, num1[:-1].split("+"))
        real2, imaginary2 = map(int, num2[:-1].split("+"))
                
        real = (real1 * real2 - imaginary1 * imaginary2)
        imaginary = (real1 * imaginary2 + real2 * imaginary1)
        
        return f"{real}+{imaginary}i"        
        
        
        
        
        

        
        
        
        