class Solution:
    def minSteps(self, n: int) -> int:
        
        
        cache = {}
        def dp(screen, clipboard):
            if (screen, clipboard) in cache: return cache[(screen, clipboard)]
            if screen == n:
                return 0
            if screen > n:
                return float('inf')
            
            copy_paste = dp(screen + screen, screen) + 2
            paste = float('inf')
            if clipboard:
                paste = dp(screen + clipboard, clipboard) + 1
            
            cache[(screen, clipboard)] = min(copy_paste, paste)
            return cache[(screen, clipboard)]
        
        return dp(1, 0)