# 1 what is insrtion sort?
    # insertion sort is a simple sorting algorithm that builds
    #  the final sorted array (or list) one item at a time. 
    # It is much less efficient on large lists than more advanced algorithms
    #  such as quicksort, heapsort, or merge sort.
    #  However, insertion sort provides several advantages:
    # 1. Simple implementation: Jon Bentley shows a three-line C version, 
    # and a five-line optimized version
    # 2. Efficient for (quite) small data sets, much like other quadratic sorting
    #  algorithms
    # 3. More efficient in practice than most other simple quadratic (i.e., O(n2))
    # in inserting sort,  always we have to compare the current element with the previous element and then we have to swap the elements 
    # if the current element is smaller than the previous element.and we always have to start the comparison from the second element of the array.
    # we have to continue this process until the array is sorted.
    # the time complexity of insertion sort is O(n^2) and the space complexity of insertion sort is O(1). 
    # insertion sort is a stable sorting algorithm. 
    # insertion sort is an in-place sorting algorithm.
    

# 3 why we need to learn insertion sort?
# actually, insertion sort is not used in practice because it is not efficient for large data sets. 
# but it is used in practice for small data sets. 
# insertion sort is used in practice when the input array is almost sorted. 


# 4 where we can use insertion sort or where we can apply insertion sort? 
# insertion sort is used in practice when the input array is almost sorted. and we can use insertion sort when the input array is small. 
#
# 5 where used insertion sort in real life examples ? 
# insertion sort is used in practice when the input array is almost sorted. and we can use insertion sort when the input array is small.
# real-life examples of insertion sort are: 
# 1. when we have to sort the deck of cards.
# 2. when we have to sort the small number of elements.
# 3. when we have to sort the data that is almost sorted.
# 4. when we have to sort the data that is continuously coming.
# 5. when we have to sort the data that is continuously coming and the data is small.
# 6. when we have to sort the data that is continuously coming and the data is almost sorted.
# 7. when we have to sort the data that is continuously coming and the data is small and almost sorted.

# 6 what are the advantages of insertion sort?
# 1. insertion sort is a simple sorting algorithm.
# 2. insertion sort is efficient for small data sets.
# 3. insertion sort is more efficient in practice than most other simple quadratic sorting algorithms.
# 4. insertion sort is an in-place sorting algorithm.
# 5. insertion sort is a stable sorting algorithm.
# 6. insertion sort is an adaptive sorting algorithm.
# 7. insertion sort is a good choice when the input array is almost sorted.
# 8. insertion sort is a good choice when the input array is small.
# disadvantages of insertion sort:
# 1. insertion sort is not efficient for large data sets.
# 2. insertion sort is not efficient for unsorted data.
# 3. insertion sort is not efficient for large data sets.
# 4. insertion sort is not efficient for unsorted data.
# 5. insertion sort is not efficient for large data sets.
#--------------------------------------------------------------------------------
# how insertion sort works? 
#--------------------------------------------------------------------------------
# 1. we have to start the comparison from the second element of the array.
# example:
# arr = [12, 11, 13, 5, 6]
# we have to start the comparison from the second element of the array.  i.e 11 and 12 
# 11 < 12 so we have to swap the elements.  i.e 11, 12, 13, 5, 6
# 2. we have to compare the current element with the previous element and then we have to swap the elements if the current element is smaller than the previous element.
#.......................................................................................................................
# implementation of insertion sort in python
#.......................................................................................................................
#.......................................................................................................................
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))
#....................................................................................................................... 
# output:
# [5, 6, 11, 12, 13]
#.......................................................................................................................
# time complexity of insertion sort:
# best case time complexity of insertion sort: O(n)
# average case time complexity of insertion sort: O(n^2)
# worst case time complexity of insertion sort: O(n^2)
# space complexity of insertion sort: O(1)
#
#.......................................................................................................................
# code working explanation and dry run and live visualization of each step of the code 
# arr = [12, 11, 13, 5, 6]
# 1 run function insertion_sort(arr)
# 2 set i = 1 and key = 11
# 3 set j = 0

#........................................................................................... ............................
# code working explanation and dry run and live visualization of each step of the code 
# in the following link: https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html
# in the following link: https://www.toptal.com/developers/sorting-algorithms/insertion-sort
#.......................................................................................................................

#.......................................................................................................................
# test the code with the following test cases
#.......................................................................................................................
# test case 1:
arr = [12, 11, 13, 5, 6]   
print(insertion_sort(arr))
# output:
# [5, 6, 11, 12, 13]
#.......................................................................................................................
# test case 2:
arr = [5, 2, 3, 1]
print(insertion_sort(arr))
# output:
# [1, 2, 3, 5]
#.......................................................................................................................
# test case 3:
arr = [5, 1, 1, 2, 0, 0]
print(insertion_sort(arr))
# output:
# [0, 0, 1, 1, 2, 5]
#.......................................................................................................................



#.......................................................................................................................
# my own code is here:
a = [4, 2, 11, 3]
for j in range(1, len(a)):
    key = a[j]
    i = j - 1
    while i >= 0 and a[i] > key:
        a[i + 1] = a[i]
        i = i - 1
    a[i + 1] = key
print(a)  # This will print the sorted array
# its time complexity is O(n^2) and space complexity is O(1)
#.......................................................................................................................
# output:
# [2, 3, 4, 11]

#.......................................................................................................................
# code working explanation and dry run and live visualization of each step of the code 

#.......................................................................................................................
# 1 create a list of a with 4 elements 4, 2, 11, 3 and store it in a variable a and its index is 0, 1, 2, 3
# 2 start the for loop from 1 to 4 and its index is 1, 2, 3 and 0 is not included in the for loop because we have to start the comparison from the second element of the array.
# 3 set key = a[1] i.e 2 and i = 0  and a[0] = 4 and 4 > 2 so we have to swap the elements i.e a[1] = 4 and a[0] = 2
# 4 set key = a[2] i.e 11 and i = 1 and a[1] = 4 and 4 < 11 so we have to swap the elements i.e a[2] = 4 and a[1] = 11
# 5 set key = a[3] i.e 3 and i = 2 and a[2] = 4 and 4 > 3 so we have to swap the elements i.e a[3] = 4 and a[2] = 3
# 6 print the sorted array i.e [2, 3, 4, 11]
#.......................................................................................................................
# 