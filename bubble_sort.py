#!/usr/bin/env python3

# Time complexity: O(n^2)
def bubble_sort(dataset: list[int]) -> list[int]:
    if len(dataset) <= 1:
        return dataset

    for i in range(len(dataset)-1, 0, -1):
        swapped = False
        for j in range(i):
            if dataset[j] > dataset[j + 1]:
                dataset[j], dataset[j + 1] = dataset[j+1], dataset[j]
                swapped = True
        # no swaps means sorted       
        if not swapped:
            break

    return dataset