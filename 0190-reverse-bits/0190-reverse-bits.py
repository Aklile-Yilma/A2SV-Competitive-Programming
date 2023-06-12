class Solution:
    def reverseBits(self, n: int) -> int:
        
        num = bin(n)[2:]
        num = num[::-1]
        num_list = list(num)
        
        while len(num_list) < 32:
            num_list.append('0')
        
        num = ''.join(num_list)
        return int(num, 2)