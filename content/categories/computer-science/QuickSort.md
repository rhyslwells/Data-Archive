---
aliases:
- null
category: CS
date modified: 27-09-2025
tags:
- algorithm
---
## [[Recursive Algorithm]]

[Quicksort Algorithm in Five Lines of Code! - Computerphile](https://www.youtube.com/watch?v=OKc2hAmMOY4)

Fast algorithm (compared to say Insertion Sort)

1) Pick pivot value
2) Divide remaining numbers into two parts
3) ==sort sublists in some way== <- apply alog again
4) merge

Recursion stops when nothing to pick for pivot value.


```python
def quick_sort(arr, depth=0):
    indent = "  " * depth  # Indentation for better readability in recursion
    print(f"{indent}Sorting: {arr}")
    
    if len(arr) <= 1:
        print(f"{indent}Returning sorted: {arr}")
        return arr  # Base case: already sorted

    pivot = arr[len(arr) // 2]  # Choosing pivot (middle element)
    left = [x for x in arr if x < pivot]  # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot
    
    print(f"{indent}Pivot: {pivot}")
    print(f"{indent}Left: {left}")
    print(f"{indent}Middle: {middle}")
    print(f"{indent}Right: {right}")
    
    sorted_left = quick_sort(left, depth + 1)
    sorted_right = quick_sort(right, depth + 1)
    
    sorted_array = sorted_left + middle + sorted_right
    print(f"{indent}Merged: {sorted_array}")
    
    return sorted_array  # Recursively sort and merge

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
print("Starting QuickSort...\n")
sorted_arr = quick_sort(arr)
print("\nFinal sorted array:", sorted_arr)
```