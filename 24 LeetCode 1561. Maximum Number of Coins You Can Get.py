from typing import *

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        res = 0
        
        for i in range(len(piles) // 3, len(piles), 2):
            res += piles[i]
            
        return res
                








 #TIme limit exceeded since min, max and remove search through a list to find it
# class Solution:
#     def maxCoins(self, piles: List[int]) -> int:
        
#         piles.sort()
#         triplet = []
        
#         my_coins = 0
        
#         while(len(piles)!=0):
#             alice = piles[-1]
#             piles.remove(alice)

#             my_coin = piles[-1]
#             my_coins+=my_coin
#             piles.remove(my_coin)

#             bob_coin = piles[0]
#             piles.remove(bob_coin)

#             triplet.append((bob_coin, my_coin, alice))
        

#         return my_coins



