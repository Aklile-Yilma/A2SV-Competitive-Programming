class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        from sortedcontainers import SortedList
        s = SortedList()
        total = 0
        
        for num in instructions:
            cost = min(s.bisect_left(num), len(s) - s.bisect_right(num))
            total += cost
            s.add(num)
        
        return total % (10 ** 9 + 7)