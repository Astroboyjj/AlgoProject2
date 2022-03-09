# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:39:44 2022

@author: Jacob Jeffery, Keondre Johnson
"""

"""
Bubble Sort -
    Desc: Sorts an array using bubble sort
    Parameters:
        arr - array to be sorted
        
CODE FROM: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
"""
def bubble_sort(arr):
    #Swaps two given indexes
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                    
    return arr

"""
Quick Sort -
    Desc: Sorts an array using quick sort
    Parameters:
        arr - array to be sorted
    
CODE FROM: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
"""
def partition(array, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return quick_sort_recursion(array, begin, end)

"""
Merge Sort -
    Desc: Sorts an array using merge sort
    Parameters:
        arr - array to be sorted
    
CODE FROM: https://www.geeksforgeeks.org/merge-sort/
"""
def merge_sort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        merge_sort(L)
  
        # Sorting the second half
        merge_sort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
"""
Radix Sort -
    Desc: Sorts an array using radix sort
    Parameters:
        arr - array to be sorted
    
CODE FROM: https://www.geeksforgeeks.org/python-program-for-radix-sort/
# This code is contributed by Mohit Kumra
# This code is updated by Sudeep Saxena(saxenasudeepcse@gmail.com) on July 9, 2020
"""
# A function to do counting sort of arr[] according to
# the digit represented by exp.
def countingSort(arr, exp1):
   
    n = len(arr)
   
    # The output array elements that will have sorted arr
    output = [0] * (n)
   
    # initialize count array as 0
    count = [0] * (10)
   
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i]/exp1)
        count[int((index)%10)] += 1
   
    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1,10):
        count[i] += count[i-1]
   
    # Build the output array
    i = n-1
    while i>=0:
        index = (arr[i]/exp1)
        output[ count[ int((index)%10) ] - 1] = arr[i]
        count[int((index)%10)] -= 1
        i -= 1
   
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]
 
# Method to do Radix Sort
def radix_sort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)
    # Counting sort every digit. Instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10
        
        
def main():
    pass


# Calling Main
main()