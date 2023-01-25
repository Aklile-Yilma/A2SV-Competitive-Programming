class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        triplet = []
        
        my_coins = 0
        
        while(len(piles)!=0):
            alice = piles[-1]
            piles.pop()

            my_coin = piles[-1]
            my_coins+=my_coin
            piles.pop()

            bob_coin = piles[0]
            piles.pop(0)

            triplet.append((bob_coin, my_coin, alice))
        

        return my_coins
            
        
        