# Select Sort
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for first_idx in range(len(names)-1):
            for idx in range(first_idx, len(names)):
                second_idx = idx 
                    
                if(heights[first_idx] < heights[second_idx]):
                    names[first_idx], names[second_idx] = names[second_idx], names[first_idx]
                    heights[first_idx], heights[second_idx] = heights[second_idx], heights[first_idx]  
                        
        return names
    
# Bubble sort
# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:      
        
#         for idx in range(len(names)):
#             is_swapped = False
#             for idx2 in range(len(names)-1):
#                 first_idx = idx2
#                 second_idx = idx2 + 1
                
#                 if(heights[idx2] < heights[idx2+1]):
#                     names[first_idx], names[second_idx] = names[second_idx], names[first_idx]
#                     heights[first_idx], heights[second_idx] = heights[second_idx], heights[first_idx]  
#                     is_swapped = True
                    
#             if not is_swapped:
#                 break
                
#         return names
                    

                