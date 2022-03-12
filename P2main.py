# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:39:44 2022

@author: Jacob Jeffery, Keondre Johnson, Jacob Theriot
"""
from Timer import Timer
import random

"""
Bubble Sort -
    Desc: Sorts an array using bubble sort
    Parameters:
        arr - array to be sorted
        
CODE FROM: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
"""
def bubbleSort(arr):
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

def quickSort(array, begin=0, end=None):
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
def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
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
def radixSort(arr):
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

    #creates the timer object for timing our sorts
    #timer.start() will start the timer (run this before you call the sort)
    #timer.stop() will stop the timer and display the time (run this right after calling sort)
    #example:
        #timer.start()
        #radix_sort(arr)
        #timer.stop()
    timer = Timer()
    
    # Introduction for CLI
    print("-----Algorithms Project 2: Sorting Algorithm Evaluation-----")
    # This creates a random array of integers from 1-100
    print("-Generating Random Data-")
    rand_array = [i for i in range(1,101)]
    random.shuffle(rand_array)
    
    # CLI for chosing the soring algorithms
    print("Which algorithm would you like to try?")
    print("Type the letter for that sort found inside the parentheses before the name of the sort.")
    print("(B) Bubble Sort")
    print("(Q) Quick Sort")
    print("(M) Merge Sort")
    print("(R) Radix Sort")
    choice = input()
    
    # This starts the timer, runs the selected sort, and stops the timer
    if choice == 'B' or choice == 'b':
        print("Bubble Sort was selected!")
        timer.start()
        bubbleSort(rand_array)
        timer.stop()
        file_name = 'P2outputB.txt'
    elif choice == 'Q' or choice == 'q':
        print("Quick Sort was selected!")
        timer.start()
        quickSort(rand_array)
        timer.stop()
        file_name = 'P2outputQ.txt'
    elif choice == 'M' or choice == 'm':
        print("Merge Sort was selected!")
        timer.start()
        mergeSort(rand_array)
        timer.stop()  
        file_name = 'P2outputM.txt'
    elif choice == 'R' or choice == 'r':
        print("Radix Sort was selected!")
        timer.start()
        radixSort(rand_array)
        timer.stop()
        file_name = 'P2outputR.txt'
    else:
        print("I didn't understand. \nPlease use the letters found in the parentheses before the name of the sort.")
       
    #temp
    timeVar = 100
    
    # This creates an output file named "P2output.txt" with the sorted array and the time
    output_file = open(file_name, 'w')
    output_file.write(str(rand_array))
    output_file.write("\nTime(seconds): " + str(timeVar))
    output_file.close()
    


# Calling Main
main()