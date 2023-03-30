# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         result = []
#         counter = list(Counter(nums).items())
        
#         def quick_sort(start, end, arr):
#             nonlocal k, result
#             if end - start + 1 <= 1:
#                 if k:
#                     result.append(arr[end][0])
#                     k -= 1
#                 return arr
            
            
#             pivot_idx = start
#             left = start
#             pivot = arr[start][1]
            
#             #partition
#             for right in range(start, end+1):
#                 if arr[right][1] <= pivot:
#                     arr[left], arr[right] = arr[right], arr[left]
#                     left += 1
                
#             left -= 1
#             arr[pivot_idx], arr[left] = arr[left], arr[pivot_idx]
                        
#             if not k:
#                 return
#             else:
#                 quick_sort(left+1, end, arr)
#                 quick_sort(start, left-1, arr)

#             return arr
        
#         quick_sort(0, len(counter)-1, counter)
        
#         return result
    

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        counter = Counter(nums)
        print(counter)
        result = []
        
        
        for key in sorted(counter, key = counter.get, reverse = True):
            if(k<1):
                break
            else:
                result.append(key)
                k-=1
                
        return result
            
        
        
            
            
        
        