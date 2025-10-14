def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list = sorted_list + left[i:]
    sorted_list = sorted_list + right[j:]

    return sorted_list

nums = [8, 3, 1, 7, 0, 10, 2, 23, 11, 18]
print("Original:", nums)
print("Sorted:", merge_sort(nums))