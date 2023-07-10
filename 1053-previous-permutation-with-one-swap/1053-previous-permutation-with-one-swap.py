class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        for i in range(n-2,-1,-1):
            if arr[i] > arr[i+1]:
                for j in range(n-1,i,-1):
                    if arr[j] < arr[i] and (j == i-1 or arr[j] != arr[j-1]):
                        arr[i],arr[j] = arr[j],arr[i]
                        return arr
        return arr