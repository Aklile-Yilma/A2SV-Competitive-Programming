class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        # base case: when n reaches 4 or 1
        if n == 1:
            return True
        
        if n < 1:
            return False
        
        if n%4 != 0:
            return False
        
        
        # Recusive case: call function with the next n/4 
        return self.isPowerOfFour(n//4)
        

# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         target = n
#         def helper(curr_num, target):
#             #base case
#             if curr_num == target:
#                 return True
#             if target < curr_num:
#                 return False
            
#             return helper( curr_num * 4 , target)
            
#         return helper(1, target)


# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
        
#         # base case: when n reaches 4 or 1
#         if n == 1:
#             return True
        
#         if n < 4:
#             return False
        
#         # Recusive case: call function with the next n/4 
#         return self.isPowerOfFour(n/4)