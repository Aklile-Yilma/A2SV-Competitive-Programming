class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_types = Counter()
        distinct = 0
        max_fruits = 0
        
        left = right = 0
        while right < len(fruits):
            # check if it is a new fruit, and update the counter
            if fruit_types[fruits[right]] == 0:
                distinct += 1
            fruit_types[fruits[right]] += 1
            
            # too many different fruits, so start shrinking window
            while distinct > 2:
                fruit_types[fruits[left]] -= 1
                if fruit_types[fruits[left]] == 0:
                    distinct -= 1
                left += 1
            
            # set max_fruits to the max window size
            max_fruits = max(max_fruits, right-left+1)
            right += 1
        
        return max_fruits

s = Solution()
print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))