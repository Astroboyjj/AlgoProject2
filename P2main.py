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
        
CODE ADAPTED FROM: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889
"""
def bubbleSort(arr):
    
    n = len(arr)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                #Swaps two indexes
                arr[i-1], arr[i] = arr[i], arr[i-1]
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
Heap Sort -

Desc: Sorts an array using heap sort
Parameters:
    arr - array to be sorted
CODE FROM: https://www.geeksforgeeks.org/heap-sort/
"""    
 # Python program for implementation of heap Sort
# To heapify subtree rooted at index i.
# n is size of heap
 
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  #swap root
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
        
def main():

    #creates the timer object for timing our sorts
    #timer.start() will start the timer (run this before you call the sort)
    #timer.stop() will stop the timer and display the time (run this right after calling sort)
    #example:
        #timer.start()
        #heap_sort(arr)
        #timer.stop()
    timer = Timer()
    
    # Introduction for CLI
    print("-----Algorithms Project 2: Sorting Algorithm Evaluation-----")
    
    # Loop and loop control for the main program
    stillRunning = True
    while(stillRunning):
        
        # input and calculation for the data set size. formula is 100 * (10 * x) where x is the input value
        print("How large do you want your data set?")
        print("The size of the set will be 100 * (10 * x) with x being the number you choose:")
        data_size = input()
        if not data_size.isnumeric():
            while(not data_size.isnumeric()):
                print("Please input an integer:")
                data_size = input()
        data_size = int(data_size)
            
        data_size = (100 * (10 * data_size))
        print("You selected a data size of " + str(data_size))
        data_size = data_size + 1 # This is to make sure the data is from 1-data_size for the range function
       
        # This creates a random array of integers from 1 to the data size. (range(1,101) would create an array of numbers from 1-100)
        print("-Generating Random Data-")
        rand_array = [i for i in range(1,data_size)]
        random.shuffle(rand_array)
        
        # CLI for chosing the soring algorithms
        print("Which algorithm would you like to try?")
        print("Type the letter for that sort found inside the parentheses before the name of the sort.")
        print("(B) Bubble Sort")
        print("(Q) Quick Sort")
        print("(M) Merge Sort")
        print("(H) Heap Sort")
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
        elif choice == 'H' or choice == 'h':
            print("Heap Sort was selected!")
            timer.start()
            heapSort(rand_array)
            timer.stop()
            file_name = 'P2outputH.txt'
        else:
            print("I didn't understand. \nPlease use the letters found in the parentheses before the name of the sort.")
            
        #temp
        timeVar = 100
        
        # This creates an output file with the sorted array and the time
        output_file = open(file_name, 'w')
        output_file.write(str(rand_array))
        output_file.write("\nTime(seconds): " + str(timeVar))
        output_file.close()
        
        # Prompt for ending the program
        new_data_control = True
        while(new_data_control):
            print("Would you like a new data set?(y/n):")
            new_data_choice = input()
            if new_data_choice == 'n' or new_data_choice == 'N':
                stillRunning = False
                new_data_control = False
            elif new_data_choice == 'y' or new_data_choice == 'Y':
                new_data_control = False
            else:
                print("I didn't understand. Please type the letter 'y' for yes or the letter 'n' for no.")
    


# Calling Main
main()