class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        nums_map = {}
        for idx, num in enumerate(nums):
            nums_map[num] = idx
            
            
        print(nums_map)
        
        for num, replacement in operations:
            idx = nums_map[num]
            del nums_map[num]
            nums_map[replacement] = idx
            
        print(nums_map)
        
        # sort with values and return only the keys
        return dict(sorted(nums_map.items(), key=lambda x: x[1])).keys()
            
            
            
        