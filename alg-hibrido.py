import random
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[len(arr) // 2]
        esq = [x for x in arr if x < pivo]
        meio = [x for x in arr if x == pivo]
        dir = [x for x in arr if x > pivo]
        return quick_sort(esq) + meio + quick_sort(dir)

def hybrid_quick_selection_sort(arr, threshold):
    hybrid_sort(arr, 0, len(arr) - 1, threshold)

def median_of_three(arr, low, high):
    mid = (low + high) // 2
    pivot_candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
    pivot_candidates.sort(key=lambda x: x[0])
    return pivot_candidates[1][1]

def selection_sort_sublist(arr, low, high):
    for i in range(low, high + 1):
        min_index = i
        for j in range(i + 1, high + 1):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def hybrid_sort(arr, low, high, threshold):
    if high - low + 1 <= threshold:
        selection_sort_sublist(arr, low, high)
    else:
        pivot_index = median_of_three(arr, low, high)
        arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
        pivot = arr[low]
        i = low + 1
        for j in range(low + 1, high + 1):
            if arr[j] < pivot:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
        arr[low], arr[i - 1] = arr[i - 1], arr[low]
        hybrid_sort(arr, low, i - 2, threshold)
        hybrid_sort(arr, i, high, threshold)

def generate_random_list(size):
    return [random.randint(0, 1000000) for _ in range(size)]

def measure_time(sort_function, arr, *args):
    start_time = time.time()
    if args:
        sort_function(arr, *args)
    else:
        sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Tamanhos dos conjuntos de dados
sizes = [1000, 10000, 50000, 500000]
num_tests = 5  # Número de testes para média

for size in sizes:
    selection_times = []
    quick_times = []
    hybrid16_times = []
    hybrid64_times = []
    hybrid256_times = []
    
    for _ in range(num_tests):
        data = generate_random_list(size)
        
        # Medir tempo para Selection Sort
        selection_data = data[:]
        selection_time = measure_time(selection_sort, selection_data)
        selection_times.append(selection_time)
        
        # Medir tempo para Quick Sort
        quick_data = data[:]
        quick_time = measure_time(quick_sort, quick_data)
        quick_times.append(quick_time)
        
        # Medir tempo para Hybrid Sort (16)
        hybrid16_data = data[:]
        hybrid16_time = measure_time(hybrid_quick_selection_sort, hybrid16_data, 16)
        hybrid16_times.append(hybrid16_time)
        
        # Medir tempo para Hybrid Sort (64)
        hybrid64_data = data[:]
        hybrid64_time = measure_time(hybrid_quick_selection_sort, hybrid64_data, 64)
        hybrid64_times.append(hybrid64_time)
        
        # Medir tempo para Hybrid Sort (256)
        hybrid256_data = data[:]
        hybrid256_time = measure_time(hybrid_quick_selection_sort, hybrid256_data, 256)
        hybrid256_times.append(hybrid256_time)
    
    print(f"Conjunto de Dados: {size} elementos")
    print(f"Tempo médio Selection Sort: {sum(selection_times) / num_tests:.6f} segundos")
    print(f"Tempo médio Quick Sort: {sum(quick_times) / num_tests:.6f} segundos")
    print(f"Tempo médio Hybrid Sort (16): {sum(hybrid16_times) / num_tests:.6f} segundos")
    print(f"Tempo médio Hybrid Sort (64): {sum(hybrid64_times) / num_tests:.6f} segundos")
    print(f"Tempo médio Hybrid Sort (256): {sum(hybrid256_times) / num_tests:.6f} segundos")
    print()
