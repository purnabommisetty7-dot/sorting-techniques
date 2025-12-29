def bubbleSort(arr):
    n=len(arr)
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            if arr[j]>arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
arr=[5,2,9,0,8]
print(bubbleSort(arr))