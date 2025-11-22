import os
import shutil
from copydetect import CopyDetector

def porownaj_stringi(kod1, kod2):
    # 1. Tworzymy tymczasowy folder
    temp_dir = "temp_compare"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # 2. Zapisujemy stringi jako pliki .py w tym folderze
    # Ważne: muszą mieć rozszerzenie (np. .py), żeby copydetect wiedział jak je czytać
    with open(f"{temp_dir}/plik1.py", "w", encoding="utf-8") as f:
        f.write(kod1)

    with open(f"{temp_dir}/plik2.py", "w", encoding="utf-8") as f:
        f.write(kod2)

    # 3. Konfigurujemy detektor
    detector = CopyDetector(
        test_dirs=[temp_dir],
        extensions=["py"],
        display_t=0,  # Licz wszystko, nawet małe podobieństwa
        silent=True  # Nie wyświetlaj paska postępu w konsoli
    )

    # 4. Uruchamiamy sprawdzanie
    detector.run()

    # 5. Wyciągamy wynik z macierzy podobieństwa
    # Macierz to tabela porównująca każdy plik z każdym.
    # [0, 1] oznacza porównanie pierwszego pliku z drugim.
    # Wynik jest w formacie: [podobienstwo_dla_pliku_1, podobienstwo_dla_pliku_2, ...]
    # Interesuje nas pierwsza wartość (index 0), która mówi ile % pliku 1 jest w pliku 2.
    score = detector.similarity_matrix[0][1][0]

    # 6. Sprzątanie (usuwanie folderu tymczasowego)
    # shutil.rmtree(temp_dir) # Odkomentuj, jeśli chcesz usuwać pliki po teście

    return score   # Zwracamy wynik w procentach


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


procent = porownaj_stringi(orig, fake)
print(f"Podobieństwo kodu: {procent:.2f}%")