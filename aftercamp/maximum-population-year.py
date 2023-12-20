class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101

        for log in logs:
            birth_idx = log[0] - 1950
            death_idx = log[1] - 1950

            for i in range(birth_idx, death_idx):
                years[i] += 1
                
        max_pop = 0
        max_idx = 0

        for idx,year in enumerate(years):
            if year > max_pop:
                max_pop = year
                max_idx = idx
        

        return max_idx + 1950