# introduct the master theorem for solving the recurrences of the form T(n) = aT(n/b) + f(n) 
# where a >= 1, b > 1 and f(n) is a given function 
# The master theorem provides a "cookbook" method for solving such recurrences  
# The master theorem has three cases, each of which gives the solution to a different type of recurrence
# The master theorem is a useful tool for analyzing the running time of divide-and-conquer algorithms 
# such as the merge sort algorithm and the binary search algorithm
# The master theorem is also useful for analyzing the running time of algorithms that use the "divide-and-conquer" paradigm
# such as the fast Fourier transform (FFT) algorithm and the Karatsuba algorithm for multiplying large integers 


# The master theorem has three cases, each of which gives the solution to a different type of recurrence 
# The three cases of the master theorem are as follows:
# Case 1: If f(n) = O(n^(log_b(a - ε))) for some constant ε > 0, then T(n) = Θ(n^(log_b(a)))

# Case 2: If f(n) = Θ(n^(log_b(a))), then T(n) = Θ(n^(log_b(a)) * log(n))
# Case 3: If f(n) = Ω(n^(log_b(a + ε))) for some constant ε > 0, and if a * f(n/b) <= c * f(n) for some constant c < 1 and sufficiently large n, then T(n) = Θ(f(n))

# .......................................................................................................................


# here is more simplified version of the master theorem 
# if nlog_b(a) > f(n), then T(n) = Θ(n^(log_b(a))) #1
# if nlog_b(a) = f(n), then T(n) = Θ(n^(log_b(a)) * log(n)) or T(n) = Θ(nlog(n)) #2
# if nlog_b(a) < f(n), then T(n) = Θ(f(n))  #3


# .......................................................................................................................
#1 prof of the master theorem (if nlog_b(a) > f(n), then T(n) = Θ(n^(log_b(a))))
# The proof of the master theorem is based on the substitution method
# The substitution method is a technique for solving recurrences   
# what is f(n) ?
# f(n) is the cost of the work done outside of the recursive calls
# Example: T(n) = 2T(n/2) + n # f(n) = n  (the cost of the work done outside of the recursive calls) 
# The substitution method is based on the following steps: 

# example of (if nlog_b(a) > f(n), then T(n) = Θ(n^(log_b(a)))) step by step
# T(n) = 2T(n/2) + n  
# a = 2, b = 2, f(n) = n  (step 1 is to identify a, b, and f(n))
# nlog_b(a) = nlog_2(2)  (step 2 put a, b, and n into the formula)
# nlog_b(a) = n^1 = n  (step 3 simplify the formula)          # nlog_b(a) = n^1 = n
# f(n) = n  (step 4 is to identify f(n))
# nlog_b(a) > f(n)  (step 5 compare nlog_b(a) and f(n))       # nlog_b(a) > f(n)
# T(n) = Θ(n^(log_b(a)))  (step 6 if nlog_b(a) > f(n), then T(n) = Θ(n^(log_b(a))))  # T(n) = Θ(n^(log_b(a)))

#  let compare the result with some puting some raondom values  in step 5  (nlog_b(a) > f(n))
# if n=6 




# .......................................................................................................................
# T(n)=2T(n/4)+n.
# a=2, b=4, f(n)=n 
# nlog_b(a)=nlog_4(2)=n^0.5 
# f(n)=n 
# nlog_b(a)>f(n) 
# T(n)=Θ(n^0.5) #  or omega( n)



