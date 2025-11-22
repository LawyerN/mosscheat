import jaccard
import lcs
import moss

orig = """
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        R[j] = arr[m + 1 + j]

    print(f"left array {' '.join(map(str, L))} right array {' '.join(map(str, R))}")

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
"""


fake = """
def _allocate_and_fill_buffers(source, left_idx, mid_idx, right_idx):
    size_a = mid_idx - left_idx + 1
    size_b = right_idx - mid_idx

    left_buffer = [0] * size_a
    right_buffer = [0] * size_b

    for x in range(size_a):
        left_buffer[x] = source[left_idx + x]
        
    for y in range(size_b):
        right_buffer[y] = source[mid_idx + 1 + y]
        
    return left_buffer, right_buffer, size_a, size_b

def _execute_merge_logic(target_arr, left_buf, right_buf, count_a, count_b, start_k):
    ptr_a = 0
    ptr_b = 0
    ptr_main = start_k

    while ptr_a < count_a and ptr_b < count_b:
        if left_buf[ptr_a] <= right_buf[ptr_b]:
            target_arr[ptr_main] = left_buf[ptr_a]
            ptr_a += 1
        else:
            target_arr[ptr_main] = right_buf[ptr_b]
            ptr_b += 1
        ptr_main += 1
        
    return ptr_a, ptr_b, ptr_main

def _finalize_remaining_items(target_arr, left_buf, right_buf, ptr_a, ptr_b, ptr_main, count_a, count_b):
    while ptr_a < count_a:
        target_arr[ptr_main] = left_buf[ptr_a]
        ptr_a += 1
        ptr_main += 1
        
    while ptr_b < count_b:
        target_arr[ptr_main] = right_buf[ptr_b]
        ptr_b += 1
        ptr_main += 1

def merge(arr, l, m, r):
  
    L_temp, R_temp, size_1, size_2 = _allocate_and_fill_buffers(arr, l, m, r)
        
    print(f"left array {' '.join(map(str, L_temp))} right array {' '.join(map(str, R_temp))}")

    idx_l, idx_r, idx_k = _execute_merge_logic(arr, L_temp, R_temp, size_1, size_2, l)

    _finalize_remaining_items(arr, L_temp, R_temp, idx_l, idx_r, idx_k, size_1, size_2)

def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
"""

mos = moss.MossDetector.compute_similarity(orig, fake, "python", "merge_sort", "merge_sort_with_changed_matchcases" )
print(mos)
spr = lcs.compute_lcs(orig, fake)
spr2 = jaccard.compute_jaccard_similarity(orig, fake, 3)
print(spr)
print(spr2)
