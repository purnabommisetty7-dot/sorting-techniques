def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
arr=[1,8,5,0,2]
print(selectionSort(arr))