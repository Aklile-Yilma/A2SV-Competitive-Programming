class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n+1)]

        num_players = n
        index = 1
        temp_k = k

        while num_players > 1:
            if players[index-1]:
                temp_k -= 1
                if temp_k == 0:
                    players[index-1] = None
                    temp_k = k
                    num_players -= 1

            index += 1
            if index > n:
                index = 1

        for num in players:
            if num:
                return num