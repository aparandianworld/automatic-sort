#!/usr/env/bin/env python3

import random

def quick_sort(dataset: list[int]) -> list[int]:
    if len(dataset) <= 1:
        return dataset
    
    # select pivot 
    pivot_index = random.randint(0, len(dataset)-1)
    pivot = dataset[pivot_index]
    
    # partition
    less = [x for i, x in enumerate(dataset) if x < pivot and i != pivot_index]
    equal = [x for i, x in enumerate(dataset) if x == pivot]
    greater = [x for i, x in enumerate(dataset) if x > pivot and i != pivot_index]
    
    return quick_sort(less) + equal + quick_sort(greater)