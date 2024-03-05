#what is searching algorithm? 
#Searching is the process of finding some particular element in the list.
#What is the purpose of searching algorithm?
#The purpose of searching algorithm is to find the location of an element in a list.
#What are the types of searching algorithm?
#There are two types of searching algorithm:
#1. Linear Search
#2. Binary Search
#What is linear search?
#Linear search is a simple searching algorithm. In this type of searching,
#  each element is compared with the element to be searched.
# This algorithm is not suitable for large data sets as it is not efficient.
# example of linear search algorithm
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
print(linear_search(data, target))
#output: True
# working of linear search algorithm
#In the above example, the linear search algorithm is implemented using a for loop.
#The algorithm searches for the target element in the data list.
# .1 def linear_search(data, target): This function takes two parameters: data and target.
#  data is the list in which the target element is to be searched and target is the element to be searched.
# .2 for i in range(len(data)): This for loop iterates through the data list.  
# .3 if data[i] == target: This condition checks if the current element of the data list is equal to the target element.
# If the condition is true, the function returns True.
# .4 return False: If the target element is not found in the data list, the function returns False.

# .....now live code visualisation of linear search algorithm above example
#.....code for linear search algorithm
# def linear_search(data, target): target = 5 data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(data)): if data[i] == target: return True return False
# 1st iteration: i=0, data[0] = 1, 1 != 5, False
# 2nd iteration: i=1, data[1] = 2, 2 != 5, False
# 3rd iteration: i=2, data[2] = 3, 3 != 5, False
# 4th iteration: i=3, data[3] = 4, 4 != 5, False
# 5th iteration: i=4, data[4] = 5, 5 == 5, True
# output: True

#What is binary search?
#Binary search is a fast search algorithm with run-time complexity of Ο(log n).
#This search algorithm works on the principle of divide and conquer.
#For this algorithm to work properly, the data collection should be in the sorted form.
#In this type of searching, the middle element is determined.
#If the middle element is the target element, then the search is complete.
#If the target element is less than the middle element, then the search continues in the lower half of the data collection.
#If the target element is greater than the middle element, then the search continues in the upper half of the data collection.
#The process continues until the target element is found or the search space is empty.
# example of binary search algorithm
def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
print(binary_search(data, target))
#output: True
# working of binary search algorithm
#In the above example, the binary search algorithm is implemented using a while loop.
#The algorithm searches for the target element in the data list.
# .1 def binary_search(data, target): This function takes two parameters: data and target.
# data is the list in which the target element is to be searched and target is the element to be searched.
# .2 low = 0 and high = len(data) - 1: These variables are used to keep track of the search space.
# low is the index of the first element and high is the index of the last element in the data list.
# .3 while low <= high: This while loop continues until the search space is empty.
# .4 mid = (low + high) // 2: This line calculates the middle index of the search space.
# .5 if data[mid] == target: This condition checks if the middle element of the search space is equal to the target element.
# If the condition is true, the function returns True.
# .6 elif data[mid] < target: This condition checks if the middle element of the search space is less than the target element.
# If the condition is true, the value of low is updated to mid + 1.
# .7 else: If the middle element of the search space is greater than the target element, the value of high is updated to mid - 1.
# .8 return False: If the target element is not found in the data list, the function returns False.

# .....now live code visualisation of binary search algorithm above example
#.....code for binary search algorithm
# def binary_search(data, target): target = 5 data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# low = 0 high = len(data) - 1
#  while low <= high: mid = (low + high) // 2 if data[mid] == target: return True
#  elif data[mid] < target: low = mid + 1 else: high = mid - 1 return False
# 1st iteration: low=0, high=9, mid=4, data[4]=5, 5==5, True
# output: True

#    recursion in binary search algorithm
#Binary search can also be implemented using recursion.
#Recursion is the process of defining something in terms of itself. 
#A function that calls itself is called a recursive function.
# example of binary search algorithm using recursion
def binary_search(data, target, low, high): # additional parameters low and high are added
    if low > high: # search space is empty  low=0, high=9  so condition is False not run and go to else part
        return False  # return False as condition is False 
    else: # search space is not empty 
        mid = (low + high) // 2 # mid = (0 + 9) // 2 = 4  mid = 4 get the middle index of the search space
        if data[mid] == target:  # data[4] = 5, 5 == 5, True
            return True     # return True as condition is True now search is complete and go to else part and return True
        elif data[mid] < target:    # data[4] = 5, 5 < 5, False
            return binary_search(data, target, mid + 1, high)
        else:
            return binary_search(data, target, low, mid - 1)
        
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
print(binary_search(data, target, 0, len(data) - 1))
#output: True


# working of binary search algorithm using recursion
#In the above example, the binary search algorithm is implemented using recursion.
#The algorithm searches for the target element in the data list.
# .1 def binary_search(data, target, low, high): This function takes four parameters: data, target, low, and high.