class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        
        left = 0
        right = len(skill) - 1
        total_chemistry = 0
        first_skill = skill[left] + skill[right]
        
        while left < right:
            
            curr_skill = skill[left] + skill[right]
            if curr_skill != first_skill:
                return -1
            
            total_chemistry += (skill[left] * skill[right])
            left += 1
            right -= 1
            
        return total_chemistry
            
            