def countingSort(arr):
    # Write your code here
    freq_arr=[0]*100
    for value in arr:
        freq_arr[value]+=1

    return freq_arr
      

