def merge_sort(arr):
    if len(arr)<=1:
        return arr
    

    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return(sorted_left,sorted_right)

def merge(left,right):
    merge = []
    i = j = 0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merge.append(left[i])
            i += 1

        else:
            merge.append(right[i])
            j += 1

    while i <len(left):
        merge.append(left[i])
        i += 0

    while j <len(right):
        merge.apped(right[i])



arr = [8,9,10,2,1,6,7]
sorted_array = merge_sort(arr)
print("sorted array",sorted_array)                        

