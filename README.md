# Ordenacao
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

def generate_random_list(size):
    return [random.randint(0, 1000000) for _ in range(size)]

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Tamanhos dos conjuntos de dados
sizes = [1000, 10000, 50000, 500000]
num_tests = 5  # Número de testes para média

for size in sizes:
    selection_times = []
    quick_times = []
    
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
    
    print(f"Conjunto de Dados: {size} elementos")
    print(f"Tempo médio Selection Sort: {sum(selection_times) / num_tests:.6f} segundos")
    print(f"Tempo médio Quick Sort: {sum(quick_times) / num_tests:.6f} segundos")
    print()
