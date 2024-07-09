Traceback (most recent call last):
  File "main.py", line 61, in <module>
    time_taken = measure_time(algo, data)
  File "main.py", line 35, in measure_time
    algorithm(data, *args)
  File "main.py", line 49, in <lambda>
    "Quick Sort": lambda arr: quicksort_hybrid(arr, 1),
  File "main.py", line 12, in quicksort_hybrid
    return quicksort_hybrid(left, lim) + middle + quicksort_hybrid(right, lim)
  File "main.py", line 12, in quicksort_hybrid
    return quicksort_hybrid(left, lim) + middle + quicksort_hybrid(right, lim)
  File "main.py", line 12, in quicksort_hybrid
    return quicksort_hybrid(left, lim) + middle + quicksort_hybrid(right, lim)
  [Previous line repeated 5 more times]
TypeError: unsupported operand type(s) for +: 'NoneType' and 'list'


** Process exited - Return Code: 1 **
Press Enter to exit terminal