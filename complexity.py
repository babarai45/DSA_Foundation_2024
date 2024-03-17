# what is time complexity? 
# why do we need to analyze the time complexity of algorithms?
# how to analyze the time complexity of algorithms?
# how to find the time complexity of any code statement?


# # what is time complexity?
# # the time complexity of an algorithm is the amount of time 
# it takes to run as a function of the length of its input.
# # it is a measure of how the running time of an algorithm 
# increases as the size of the input increases. 
# # it is an important metric to compare the efficiency of different algorithms
# # and to predict the running time of an algorithm for large inputs.

# # why do we need to analyze the time complexity of algorithms?
# # to compare the efficiency of different algorithms.
# # to predict the running time of an algorithm for large inputs.

# # how to analyze the time complexity of algorithms? 
# # there are several methods to analyze the time complexity of algorithms,
# # such as the big O notation, the recursion tree method, the master theorem,
# # and the substitution method,and the iteration method. each method has its own advantages and disadvantages.


# # how to find the time complexity of any code statement? 
# # to find the time complexity of any code statement, we can use the following steps:
# # 1. identify the basic operations in the code statement. 
# # 2. count the number of times each basic operation is executed. 
# # 3. express the total number of basic operations as a function of the input size.
# # 4. simplify the function using the big O notation.

# <--------------------------------------Tips and Tricks to Find the Time Complexity of Any Code Statement-------------------------------------->
# here is some tips and tricks to find the time complexity of any code statement:
# # 1. the time complexity of a single statement is O(1).  (constant time)
# example: a = 1;  # O(1)  (constant time) (because it is a single statement that takes constant time to execute regardless of the input size)

# # 2. the time complexity of a sequence of statements is the maximum time complexity of the individual statements.
# example: a = 1;  # O(1)  (constant time)
# b = 2;  # O(1)  (constant time)
# c = a + b;  # O(1)  (constant time)
# the time complexity of the sequence of statements is O(1)  (constant time)  (because the maximum time complexity of the individual statements is O(1))

# # 3. the time complexity of a loop is the time complexity of the body of the loop multiplied by the number of iterations of the loop. 
# example: for i in range(n):  # O(n)  (linear time)  (because the body of the loop has a time complexity of O(1) and the loop has n iterations)


# # 4. the time complexity of a nested loop is the product of the time complexities of the individual loops. 
# example: for i in range(n):  # O(n)  (linear time)
# for j in range(n):  # O(n)  (linear time)
# the time complexity of the nested loops is O(n^2)  (quadratic time)  (because the product of the time complexities of the individual loops is O(n^2))

# # 5. the time complexity of a 3-level nested loop is O(n^3)  (cubic time)
# example: for i in range(n):  # O(n)  (linear time)
# for j in range(n):  # O(n)  (linear time)
# for k in range(n):  # O(n)  (linear time)
# the time complexity of the 3-level nested loop is O(n^3)  (cubic time)  (because the product of the time complexities of the individual loops is O(n^3))

# # 6. the time complexity of a recursive algorithm can be analyzed using the recursion tree method.
# example: def factorial(n):  # O(n)  (linear time)
# if n == 0:  # O(1)  (constant time)
# return 1  # O(1)  (constant time)
# else:  # O(1)  (constant time)
# return n * factorial(n-1)  # O(n)  (linear time)
# the time complexity of the recursive algorithm is O(n)  (linear time)  (because the recursion tree has n levels and each level has a time complexity of O(1))

# # 7. the time complexity of a divide-and-conquer algorithm can be analyzed using the recursion tree method.or the master theorem.
# tips and tricks to find the time complexity for (logn) time complexity

# when every time the input size is reduced by a constant factor, the time complexity of the algorithm is O(log n)  (logarithmic time)
# example: def binary_search(arr, l, r, x):  # O(log n)  (logarithmic time)
# if r >= l:  # O(1)  (constant time) # here r is the right side of the array and l is the left side of the array
# mid = l + (r - l) // 2  # O(1)  (constant time) # here we are finding the middle element of the array
# the time complexity of the divide-and-conquer algorithm is O(log n)  (logarithmic time)  (because the time complexity of the divide-and-conquer algorithm is O(log n))
# but question is that how we can say that the time complexity of the divide-and-conquer algorithm is O(log n)  whenever both line have constant time complexity so how ?
# actually here we are dividing the array into two parts and then we are finding the middle element of the array and then we are comparing the middle element with the key element
# and then we are finding the middle element of the array and then we are comparing the middle element with the key element
# so here we are reducing the input size by a constant factor and then we are finding the middle element of the array and then we are comparing the middle element with the key element 
# this is why the time complexity of the divide-and-conquer algorithm is O(log n)  (logarithmic time)  (because the time complexity of the divide-and-conquer algorithm is O(log n))
#----------------------------------------------------
# next tips 
# when we multiply or divide the input size by a constant factor, the time complexity of the algorithm is O(log n)  (logarithmic time)
# # here is input size is a user input
# # here  constant factor is 2 like 2 * n or n / 2 
# example of this tips by code :
# user_input = int(input("Enter a number: "))  # O(1)  (constant time)
# while user_input > 1: # o(n)  (linear time)
# user_input = user_input / 2  # o(log n)  (logarithmic time ) (because we are dividing the input size by a constant factor)

# # here is input size is a user input 6
# # here  constant factor is 3 like 3 * n or n / 3
# if we calculate above code individually line by line like this :
# user_input = 6  # O(1)  (constant time)
# while user_input > 1:  # O(n)  (linear time)
# user_input = user_input / 3  # O(log n)  (logarithmic time)  (because we are dividing the input size by a constant factor)
# # how to calculate the time complexity individually line by line ?
# # 1. the time complexity of the first line is O(1)  (constant time)  (because it is a single statement that takes constant time to execute regardless of the input size)
# # 2. the time complexity of the second line is O(n)  (linear time)  (because the body of the loop has a time complexity of O(1) and the loop has n iterations)
# # 3. the time complexity of the third line is O(log n)  (logarithmic time)  (because we are dividing the input size by a constant factor)


# what (logarithmic time) time complexity of the divide-and-conquer algorithm is O(log n) ?
# A divide-and-conquer algorithm is a recursive algorithm that breaks a problem into smaller subproblems,
#  solves the subproblems, and then combines the solutions to the subproblems to solve the original problem.
# it is also called a divide-and-conquer algorithm because it divides the problem into smaller subproblems,
# solves the subproblems, and then combines the solutions to the subproblems to solve the original problem.
# the time complexity of a divide-and-conquer algorithm can be analyzed using the recursion tree method or the master theorem.
# the time complexity of the divide-and-conquer algorithm is O(log n)  (logarithmic time)  (because the time complexity of the divide-and-conquer algorithm is O(log n))




# 1- Questions to compute time complexity of code segment examples.

#example 1 (constant time) 
# code 
# a = 1;  # O(1)  (constant time) (because it is a single statement that takes constant time to execute regardless of the input size)
# what is the time complexity of this code segment?
# O(1)  (constant time)  (because it is a single statement that takes constant time to execute regardless of the input size)


# example 2 (constant time)
# code
# a = 1;  # O(1)  (constant time)
# b = 2;  # O(1)  (constant time)
# c = a + b;  # O(1)  (constant time)
# what is the time complexity of this code segment?
# O(1)  (constant time)  (because the maximum time complexity of the individual statements is O(1))





# example 3 (linear time) 
# code 
# for i in range(n):  # O(n)  (linear time)  (because the body of the loop has a time complexity of O(1) and the loop has n iterations)
# what is the time complexity of this code segment? 
# O(n)  (linear time)  (because the body of the loop has a time complexity of O(1) and the loop has n iterations)


# example 4 (quadratic time) 
# code 
# for i in range(n):  # O(n)  (linear time)
# for j in range(n):  # O(n)  (linear time)
# what is the time complexity of this code segment? 
# O(n^2)  (quadratic time)  (because the product of the time complexities of the individual loops is O(n^2))



# example 5 (cubic time)
# code
# for i in range(n):  # O(n)  (linear time)
# for j in range(n):  # O(n)  (linear time)
# for k in range(n):  # O(n)  (linear time)
# what is the time complexity of this code segment?
# O(n^3)  (cubic time)  (because the product of the time complexities of the individual loops is O(n^3))


# example 6 (linear time)
# code
# def factorial(n):  # O(n)  (linear time)
# if n == 0:  # O(1)  (constant time)   
# return 1  # O(1)  (constant time)
# else:  # O(1)  (constant time)
# return n * factorial(n-1)  # O(n)  (linear time)
# what is the time complexity of this code segment?
# O(n)  (linear time)  (because the recursion tree has n levels and each level has a time complexity of O(1))



# example 7 (logarithmic time)
# code
# def binary_search(arr, l, r, x):  # O(log n)  (logarithmic time)
# if r >= l:  # O(1)  (constant time)
# mid = l + (r - l) // 2  # O(1)  (constant time)
# what is the time complexity of this code segment?
# O(log n)  (logarithmic time)  (because the time complexity of the divide-and-conquer algorithm is O(log n))


#----------------------------------------------------



# now a  [] is more less than 1000 elements
# a make list of 1000 unsorted elements
import random
# Generating a list of 1000 unsorted elements
a = [random.randint(1, 10000) for _ in range(10000)]
# a = [4, 2, 11, 3]
# here is to function  to show total time to run the code 
import time
start = time.time()
a = [4, 2, 11, 3]
for j in range(1, len(a)):
    key = a[j]
    i = j - 1
    while i >= 0 and a[i] > key:
        a[i + 1] = a[i]
        i = i - 1
    a[i + 1] = key
print(a)  # This will print the sorted array
end = time.time()
print(end - start)  # This will print the total time to run the code in milliseconds
