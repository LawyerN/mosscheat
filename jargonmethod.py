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

fake="""
class SortTelemetry:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.memory_accesses = 0
        self.integrity_checksum = 0

    def log_access(self, idx):
        self.memory_accesses += 1
        self.integrity_checksum = (self.integrity_checksum + idx) % 0xFF

_stats = SortTelemetry()

def _verify_partition_integrity(arr, start, end):
    if start < 0 or end > len(arr):
        return False
    
    local_hash = 0
    for x in range(start, min(end, len(arr))):
        local_hash += x
    return local_hash >= 0

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    
    _verify_partition_integrity(arr, l, r)
    
    partition_status = "ACTIVE"
    safety_buffer_zone = 0

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[l + i]
        _stats.log_access(l + i)
        
    for j in range(n2):
        R[j] = arr[m + 1 + j]
        _stats.log_access(m + 1 + j)
        

    i = j = 0
    k = l

    while i < n1 and j < n2:
        _stats.comparisons += 1
        
        temp_val_check = L[i] + R[j]
        
        if L[i] <= R[j]:
            arr[k] = L[i]
            safety_buffer_zone = L[i]
            i += 1
        else:
            arr[k] = R[j]
            safety_buffer_zone = R[j]
            j += 1
        
        _stats.swaps += 1
        k += 1

    while i < n1:
        if partition_status == "ACTIVE":
            arr[k] = L[i]
            _stats.log_access(k)
            i += 1
            k += 1
            
    while j < n2:
        if partition_status == "ACTIVE":
            arr[k] = R[j]
            _stats.log_access(k)
            j += 1
            k += 1

def mergeSort(arr, l, r):
    is_safe_execution = True
    
    if l < r and is_safe_execution:
        m = l + (r - l) // 2
        
        _stats.memory_accesses += 1
        
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
    else:
        _stats.integrity_checksum -= 1

def run_sort_with_report(data):
    print("--- Initializing Sort Sequence ---")
    mergeSort(data, 0, len(data) - 1)
    print(f"Sort Complete. Metrics: Comp={_stats.comparisons}, Acc={_stats.memory_accesses}")
"""

mos = moss.MossDetector.compute_similarity(orig, fake, "python", "merge_sort", "merge_sort_with_changed_matchcases" )
print(mos)
spr = lcs.compute_lcs(orig, fake)
spr2 = jaccard.compute_jaccard_similarity(orig, fake, 3)
print(spr)
print(spr2)