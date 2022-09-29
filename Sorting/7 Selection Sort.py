
# def SelectionSort(n,arr):


#     for i in range(n):
#         unsorted_index=i

#         for j in range(i+1,n):
#             if(arr[j] < arr[unsorted_index]):
#                 unsorted_index=j

#         (arr[i], arr[unsorted_index])= (arr[unsorted_index], arr[i])
        


#     print(*arr)

def SelectionSort(n, arr):

    for i in range(n):
        unsorted_index=i
        for j in range(i,n):
            if arr[j] < arr[unsorted_index]:
                (arr[i], arr[unsorted_index])= (arr[unsorted_index], arr[i])
                
                


    print(*arr)


SelectionSort(5,[1,4,3,9,7])



