def merge_sort(arr):
    if len(arr)<=1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)

    return merge_two_sorted_arrays(left,right,arr)

def merge_two_sorted_arrays(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j += 1
        k+=1
    if i<len_a:
        while i<len_a:
            arr[k] = a[i]
            i += 1
            k+=1
    else:
        while j<len_b:
            arr[k] = b[j]
            k+=1
            j += 1
arr = [45,89,78,12,3,56,14,23,89,125,36]
merge_sort(arr)
print(arr)