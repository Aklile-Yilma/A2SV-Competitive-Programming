class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        less_pivot = []
        greater_pivot = []
        pivot_idx = nums.index(pivot)
        
        for idx, num in enumerate(nums):
            if(idx != pivot_idx):
                if(num > pivot):
                    greater_pivot.append(num)
                else:
                    #edge case for multiple pivots such that all pivots must be at the center
                    if less_pivot:
                        if less_pivot[-1] == pivot:
                            less_pivot.pop()
                            less_pivot.append(num)
                            less_pivot.append(pivot)
                            continue
                    less_pivot.append(num)

        # because it was skipped in iteration
        less_pivot.append(pivot)
        
        return less_pivot + greater_pivot
        