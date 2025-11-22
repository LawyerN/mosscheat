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
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    
    i = 0
    while i < n1:
        L[i] = arr[l + i]
        i += 1
        
   
    j = 0
    while j < n2:
        R[j] = arr[m + 1 + j]
        j += 1
        
    print(f"left array {' '.join(map(str, L))} right array {' '.join(map(str, R))}")

    i = j = 0
    k = l
    
    while True:
       
        if i >= n1 or j >= n2:
            break
            
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        
    while True:
        if i >= n1:
            break
        arr[k] = L[i]
        i += 1
        k += 1
        
    
    while True:
        if j >= n2:
            break
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

# mos = moss.MossDetector.compute_similarity(orig, fake, "python", "merge_sort", "merge_sort_with_changed_matchcases" )
# print(mos)
spr = lcs.compute_lcs(orig, fake)
spr2 = jaccard.compute_jaccard_similarity(orig, fake, 3)
print(spr)
print(spr2)
