# Implement an object-oriented structure for your program with the following classes:
# • Sorter: A base class that contains the common sorting functionality.
# • Three derived classes (InsertionSorter, BubbleSorter, and SelectionSorter) that inherit from the 
# Sorter base class and implement the specific sorting algorithms both for ascending and descending 
# order.
# Create a user-friendly command-line interface that allows users to:
# • Input the size of the dataset (an integer).
# • Enter the dataset.
# • Enter the order to sort data i.e. ascending or descending order. 
# • Choose a sorting algorithm (Insertion Sort, Bubble Sort, or Selection Sort).
# • Execute the selected sorting algorithm.
# Each derived sorting class should have a method to perform the sorting operation on the input dataset. Use 
# polymorphism to call the appropriate sorting method based on the user's choice..
# Measure and display the execution time (in milliseconds) for each sorting algorithm on datasets of varying 
# sizes (e.g., 100, 1000, 10,000 elements). Implement a function to analyze and compare the execution times. 
# Create a visually appealing output to present the results.

#.......................................................................................................................
# implementation of insertion sort in python
#.......................................................................................................................
# soultion 1 
#.......................................................................................................................
# def insert_sort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while j > 0 and arr[j - 1] > arr[j]:
#             arr[j - 1], arr[j] = arr[j], arr[j - 1]
#             j -= 1
# arr = [2, 6, 5, 1, 3, 2]
# insert_sort(arr)
# print(arr)

#.......................................................................................................................
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
# arr = [12, 11, 13, 5, 6]
# print(insertion_sort(arr))
#.......................................................................................................................
# output:
# [5, 6, 11, 12, 13]
#.......................................................................................................................
# time complexity of insertion sort:    
#.......................................................................................................................
# The time complexity of insertion sort is O(n^2) because there are two nested loops.
#.......................................................................................................................
# space complexity of insertion sort:
#.......................................................................................................................
# The space complexity of insertion sort is O(1) because the algorithm is in-place.

#.......................................................................................................................
# implementation of bubble sort in python
#.......................................................................................................................
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
# arr = [64, 34, 25, 12, 22, 11, 90]
# print(bubble_sort(arr))
#.......................................................................................................................
# output:
# [11, 12, 22, 25, 34, 64, 90]
#.......................................................................................................................
# time complexity of bubble sort:
#.......................................................................................................................
# The time complexity of bubble sort is O(n^2) because there are two nested loops.
#.......................................................................................................................
# space complexity of bubble sort:
#.......................................................................................................................
# The space complexity of bubble sort is O(1) because the algorithm is in-place.

#.......................................................................................................................
# implementation of selection sort in python
#.......................................................................................................................
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr
# arr = [64, 25, 12, 22, 11]
# print(selection_sort(arr))
#.......................................................................................................................
# output:
# [11, 12, 22, 25, 64]
#.......................................................................................................................
# time complexity of selection sort:
#.......................................................................................................................
# The time complexity of selection sort is O(n^2) because there are two nested loops.
#.......................................................................................................................
# space complexity of selection sort:
#.......................................................................................................................
# The space complexity of selection sort is O(1) because the algorithm is in-place.
#.......................................................................................................................
import time
import random

class Sorter:
    def sort(self, arr, order):
        pass

class InsertionSorter(Sorter):
    def sort(self, arr, order):
        if order == "ascending" or order == "A":
            insertion_sort_asc(arr)
        elif order == "descending" or order == "D":
            insertion_sort_desc(arr)
def insertion_sort_asc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key > arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
                
class BubbleSorter(Sorter):
    def sort(self, arr, order):
        if order == "ascending" or order == "A":
            bubble_sort_asc(arr)
        elif order == "descending" or order == "D":
            bubble_sort_desc(arr)
            
def bubble_sort_asc(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
class SelectionSorter(Sorter):
    def sort(self, arr, order):
        if order == "ascending" or order == "A":
            selection_sort_asc(arr)
        elif order == "descending" or order == "D":
            selection_sort_desc(arr)
            
def selection_sort_asc(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
def selection_sort_desc(arr):
    for i in range(len(arr)): 
        max_idx = i
        for j in range(i+1, len(arr)):
            if arr[max_idx] < arr[j]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

# Command line interface        
print("Welcome to the sorting algorithm analyzer!")

n = int(input("Enter size of dataset: "))
print("Enter the dataset (separated by spaces):")
arr = [int(x) for x in input().split()]

order = input("Enter order to sort (ascending for A or descending for D): ")

print("Choose sorting algorithm:")
print("1. Insertion Sort")
print("2. Bubble Sort")
print("3. Selection Sort")
choice = int(input("Enter choice: "))

sorter = None
if choice == 1:
    sorter = InsertionSorter()
elif choice == 2:
    sorter = BubbleSorter()  
elif choice == 3:
    sorter = SelectionSorter()
    
start = time.time()*1000
sorter.sort(arr, order) 
end = time.time()*1000
elapsed = end - start

print("Sorted array:", arr)
print("Time taken to sort:", elapsed, "ms")

print("\nAnalysis:")

sizes = [100, 1000, 10000]
for size in sizes:
    arr = [random.randint(0,1000) for i in range(size)]
    
    start = time.time()*1000
    InsertionSorter().sort(arr.copy(), order)
    end = time.time()*1000 
    time_insertion_sort = end - start
    
    start = time.time()*1000
    BubbleSorter().sort(arr.copy(), order) 
    end = time.time()*1000
    time_bubble_sort = end - start
    
    start = time.time()*1000        
    SelectionSorter().sort(arr.copy(), order)
    end = time.time()*1000
    time_selection_sort = end - start
    
    print(f"{size} elements:") 
    print(f"Insertion sort: {time_insertion_sort} ms")
    print(f"Bubble sort: {time_bubble_sort} ms")
    print(f"Selection sort: {time_selection_sort} ms")
    print()
print(""" Analysis shows that insertion sort is fastest for small datasets, 
          while bubble sort and selection sort have similar performance. 
          As dataset size increases, insertion sort becomes slower compared 
          to bubble sort and selection sort.""")
# .................................................................
# code output: 
# .................................................................
# Welcome to the sorting algorithm analyzer!
# Enter size of dataset: 5
# Enter the dataset (separated by spaces):
# 12 11 13 5 6
# Enter order to sort (ascending for A or descending for D): A
# Choose sorting algorithm:
# 1. Insertion Sort
# 2. Bubble Sort
# 3. Selection Sort
# Enter choice: 1
# Sorted array: [5, 6, 11, 12, 13]
# Time taken to sort: 0.0 ms
# time complexity of above code is O(n^2)
