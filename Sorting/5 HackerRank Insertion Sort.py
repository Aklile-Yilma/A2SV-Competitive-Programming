def insertionSort(n, arr):
    
    for right in reversed(range(2,n)):
        """key is the smaller value which is compared to the previous values to move the previous element to the next position"""
        
        key= arr[right]
        left= right-1
        
        while left>=0 and arr[left]> key:
            arr[left+1]= arr[left]
            left-=1
            print(*arr)
    
        arr[left+1]=key
    print(*arr)
        



