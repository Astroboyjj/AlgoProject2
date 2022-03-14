# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:39:44 2022

@author: Jacob Jeffery, Keondre Johnson, Jacob Theriot
"""
#from Timer import Timer
import random, time, pathlib
from pathlib import Path

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
        
# Method for running the test and writing the output to file
def runTest(test, output_file, loop_index, data, data_size):
    print("-Sorting Started-")
    
    # Run the test
    if test == "B":
        start = time.perf_counter()
        bubbleSort(data)
        end = time.perf_counter()
    elif test == "Q":
        start = time.perf_counter()
        quickSort(data)
        end = time.perf_counter()
    elif test == "M":
        start = time.perf_counter()
        mergeSort(data)
        end = time.perf_counter()
    elif test == "H":
        start = time.perf_counter()
        heapSort(data)
        end = time.perf_counter()
        
    print("-Sorting Finished-")
    print("Time: " + str(end-start))
    
    # Write the output to the output file
    output_file.write("---Analysis " + str(loop_index + 1) + "---\n")
    output_file.write("Data size: " + str(data_size - 1) + "\n")
    output_file.write("Time(seconds): " + str(end-start) + "\n")
    print("-Written to Ouput File-")
    
 # Method for worst time complexity of Merge Sort (will turn [1,2,3,4,5,6,7,8] into [5,1,7,3,6,2,8,4])
def unMerge(chunk):
    if len(chunk) > 2:
        L = chunk[::2]
        R = chunk[1::2]
        L = unMerge(L)
        R = unMerge(R)
        chunk = L + R
    elif len(chunk) == 2:
        chunk.reverse()
    return chunk
    
# Method for generating new array and sorting it
def generateDataSet(data_size, data_order):
    # This creates a random array of integers from 1 to the data size. (range(1,101) would create an array of numbers from 1-100)
    print("-Generating Random Data-")
    data_set = [i for i in range(1,data_size)]
    
    if data_order == 'random': 
        random.shuffle(data_set)
    elif data_order == 'sorted':
        pass
    elif data_order == 'reverse':
        data_set.reverse()
    elif data_order == 'mergeWorst':
        data_set = unMerge(data_set)

    return data_set
    
# Method for choosing which sorting method to use on the data set before it is tested
def chooseOrder(test):
    print("How do you want your data set sorted?")
    print("(A) Best time complexity")
    print("(B) Average time complexity")
    print("(C) Worst time complexity")
    data_order = input()
    while(not data_order == 'A' and not data_order == 'a' and not data_order == 'B' and not data_order == 'b' and not data_order == 'C' and not data_order == 'c'):
        print("Please input the letter inside the parentheses corresponding to your choice")
        data_order = input()

    # This is where the best, worst, and average case choices are defined for each algorithm
    if test == 'B' or test == 'b':
        if data_order == 'A' or data_order == 'a':
            return 'sorted'
        elif data_order == 'B' or data_order == 'b':
            return 'random'
        elif data_order == 'C' or data_order == 'c':
            return 'reverse'
    elif test == 'Q' or test == 'q':
        if data_order == 'A' or data_order == 'a':
            return 'reverse'
        elif data_order == 'B' or data_order == 'b':
            return 'random'
        elif data_order == 'C' or data_order == 'c':
            return 'sorted'
    elif test == 'M' or test == 'm':
        if data_order == 'A' or data_order == 'a':
            return 'sorted'
        elif data_order == 'B' or data_order == 'b':
            return 'random'
        elif data_order == 'C' or data_order == 'c':
            return 'mergeWorst'
    elif test == 'H' or test == 'h':
        if data_order == 'A' or data_order == 'a':
            return 'random'
        elif data_order == 'B' or data_order == 'b':
            return 'random'
        elif data_order == 'C' or data_order == 'c':
            return 'random'
        
def main():
    # This creates an output file to write our results to
    file_path = Path("./P2output.txt")
    if file_path.exists():
        output_file = open('P2output.txt', 'a')
        output_file.write("------------------------------------------------\n")
        output_file.write("------------NEW EXECUTION OF PROGRAM------------\n")
        output_file.write("------------------------------------------------\n")
    else:
        output_file = open('P2output.txt', 'x')
    
    # Introduction for CLI
    print("-----Algorithms Project 2: Sorting Algorithm Evaluation-----")
    
    # Loop and loop control for the main program
    stillRunning = True
    while(stillRunning):
        
        # input for the data set size and order.
        print("How large do you want your data set?")
        data_size = input()
        if not data_size.isnumeric():
            while(not data_size.isnumeric()):
                print("Please input an integer:")
                data_size = input()
        data_size = int(data_size)
        print("You selected a data size of " + str(data_size))
        data_size = data_size + 1 # This is to make sure the data is from 1-data_size for the range function
  
        # CLI for chosing the soring algorithms
        print("Which algorithm would you like to try? (Runs 5 times)")
        print("Type the letter for that sort found inside the parentheses before the name of the sort.")
        print("(B) Bubble Sort")
        print("(Q) Quick Sort")
        print("(M) Merge Sort")
        print("(H) Heap Sort")
        choice = input()
        while(not choice == 'Q' and not choice == 'q' and not choice == 'B' and not choice == 'b' and not choice == 'M' and not choice == 'm' and not choice == 'H' and not choice == 'h'):
            print("Please input the letter inside the parentheses corresponding to your choice")
            choice = input()
        
        data_order = chooseOrder(choice)
        
        # This starts the timer, runs the selected sort, stops the timer, then writes the output data to the file
        # Output data: Algorithm name, size of set, and time of the sort
        i = 0
        if choice == 'B' or choice == 'b':
            print("Bubble Sort was selected!")
            output_file.write("------Bubble Sort------\n")
            while(i < 5):
                data = generateDataSet(data_size, data_order)
                runTest('B', output_file, i, data, data_size)
                i = i + 1
        elif choice == 'Q' or choice == 'q':
            print("Quick Sort was selected!")
            output_file.write("------Quick Sort------\n")
            while(i < 5):
                data = generateDataSet(data_size, data_order)
                runTest('Q', output_file, i, data, data_size)
                i = i + 1
        elif choice == 'M' or choice == 'm':
            print("Merge Sort was selected!")
            output_file.write("------Merge Sort------\n")
            while(i < 5):
                data = generateDataSet(data_size, data_order)
                runTest('M', output_file, i, data, data_size)
                i = i + 1
        elif choice == 'H' or choice == 'h':
            print("Heap Sort was selected!")
            output_file.write("------Heap Sort------\n")
            while(i < 5):
                data = generateDataSet(data_size, data_order)
                runTest('H', output_file, i, data, data_size)
                i = i + 1
        else:
            print("I didn't understand. \nPlease use the letters found in the parentheses before the name of the sort.")
            
        
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
                
    # Closes and saves the output file after the program finishes
    output_file.close()
    print("Output file saved to the same location as this program.")
    


# Calling Main
main()
