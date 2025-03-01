#!/usr/bin/env python3

# Time complexity: O(n log n)
def merge_sort(dataset: list[int]) -> list[int]:
    if len(dataset) <= 1:
        return dataset
    
    midpoint = len(dataset) // 2
    left_array = merge_sort(dataset[:midpoint]) 
    right_array = merge_sort(dataset[midpoint:])
    
    left_index, right_index = 0, 0
    merged = []
    
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            merged.append(left_array[left_index])
            left_index += 1
        else: 
            merged.append(right_array[right_index])
            right_index += 1
            
    merged.extend(left_array[left_index:])
    merged.extend(right_array[right_index:])
    
    return merged