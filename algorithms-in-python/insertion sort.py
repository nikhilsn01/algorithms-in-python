def insertion_sort(arr):
    length = len(arr)
    for i in range(1,len(arr)):
        ele = arr[i]
        j = i-1
        while j>=0 and ele<arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = ele
        if length%2 == 0:
            print((arr[length//2 - 1]+arr[length//2])/2)
        else:
            print(arr[length//2])

elements = [2, 1, 5, 7, 2, 0, 5]
insertion_sort(elements)
