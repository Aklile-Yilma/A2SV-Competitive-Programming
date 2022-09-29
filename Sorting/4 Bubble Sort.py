"""
Bubble Sort is the simplest sorting algorithm that 
works by repeatedly swapping the adjacent elements
if they are in the wrong order
"""

def countSwaps(a):
    # Write your code here
    count=0
    for i in range(len(a)):
        for j in range(len(a)-1):       
            if(a[j]>a[j+1]):
                a[j],a[j+1]= a[j+1], a[j]
                count+=1
    print("Array is sorted in", count, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[len(a)-1])
    

countSwaps([1,5,3,2])
                