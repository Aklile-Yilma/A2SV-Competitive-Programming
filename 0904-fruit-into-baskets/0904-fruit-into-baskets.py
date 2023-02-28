class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0
        max_pick = 0
        fruits_map = {}
        
        for right in range(len(fruits)):
            
            fruit = fruits[right]
            
            if fruit in fruits_map:
                fruits_map[fruit] += 1
            else:
                fruits_map[fruit] = 1
                
            
            while len(fruits_map.keys()) >= 3:
                fruits_map[fruits[left]] -= 1
                if fruits_map[fruits[left]] == 0:
                    del fruits_map[fruits[left]]
                left += 1
                
            max_pick = max(max_pick, right - left + 1)
                
        return max_pick
                
            
        