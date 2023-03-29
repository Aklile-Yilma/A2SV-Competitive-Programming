num_swap = [0]
def mergeSort(left, right, arr):
    
    if left == right:
        return [arr[left]]
    
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)
    
    return merge(left_half, right_half)


def merge(arr1, arr2):

    arr3 = []
    
    if arr1[0] <= arr2[0]:
        arr3.extend(arr1)
        arr3.extend(arr2)
    else:
        arr3.extend(arr2)
        arr3.extend(arr1)
        num_swap[0] += 1
    
    return arr3


num_test_cases = int(input())

for _ in range(num_test_cases):
    size = int(input())
    arr = list(map(int, input().split()))
    
    arr = mergeSort(0, len(arr)-1, arr)    
    if sorted(arr) == arr:
        print(num_swap[0])
    else:
        print(-1)
    num_swap[0] = 0
    
