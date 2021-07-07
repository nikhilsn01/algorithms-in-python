def partition(arr,start,end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while (start<len(arr)) and(arr[start]<=pivot):
            start+=1
        while arr[end]>pivot:
            end-=1

        if start<end:
            arr[start],arr[end] = arr[end],arr[start]

    arr[pivot_index],arr[end] = arr[end],arr[pivot_index]
    return end

def quick_sort(arr,start,end):
    if start<end:
        pi = partition(arr,start,end)
        quick_sort(arr,start,pi-1)
        quick_sort(arr,pi+1,end)
elements = [11,9,29,7,2,15,28,45,21,14,24,58,94,21,56,45]
print(elements)
quick_sort(elements,0,len(elements)-1)
print(elements)