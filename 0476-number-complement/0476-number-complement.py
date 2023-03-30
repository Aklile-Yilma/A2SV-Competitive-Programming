class Solution:
    def findComplement(self, num: int) -> int:
        complementer = 1
        while num > complementer:
            complementer = (complementer << 1) + 1
        
        return num ^ complementer