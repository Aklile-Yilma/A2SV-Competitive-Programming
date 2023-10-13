class Solution:
    def knightDialer(self, n: int) -> int:
        
        knight_map = {
            0 : [4, 6],
            1 : [6, 8],
            2 : [7, 9],
            3 : [4, 8],
            4 : [0, 3, 9],
            5 : [],
            6 : [0, 1, 7],
            7 : [2, 6],
            8 : [1, 3],
            9 : [2, 4],
        }
        
        dp = {}
        
        def dfs(curr_n, x):
            
            if curr_n == 1:
                return 1
            
            if (curr_n, x) in dp:
                return dp[(curr_n, x)]
            
            ans = 0
            for child in knight_map[x]:
                ans += dfs(curr_n-1, child)
                
            dp[(curr_n, x)] = ans
            
            return dp[(curr_n, x)]
            
        ans = 0
        for num in knight_map:
            ans += dfs(n, num)
            
        return ans % (10 ** 9 + 7)