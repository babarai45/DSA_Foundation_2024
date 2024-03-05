# Question 01: (20 Points)
# CODE IN PYTHON 
# CPU scheduler simulator  
# In this programming exercise, you’ll design a CPU scheduler simulator. This simulator would use an array data 
# structure. Here is how it should work: 
# The scheduler should take in processes from a file named readylist.txt and add them to an array. The format of 
# the file would be: 
# <process_name, execution_time> 
# This file could have processes in any order. After reading in, your program should empty the file readylist.txt.
# • Once all the processes are read from the readylist.txt file into an array, your program would execute 
# each of the processes in highest-execution-time-first (the process having a highest execution time will 
# be run first) order. 
# • But before executing any process, the program should print the sorted contents of the array, and example 
# could be, 
# The contents of the ready queue are: 
# sms.exe, 23 
# mms.exe, 13 
# explorer.exe, 9 
# devmgmt.exe, 4 
# ..... 
# ..... 
# • Now it should start executing the processes in the array. For each process, execution just means that 
# process stays at the start of the array until time equal to its execution time has passed. The process is 
# deleted from the array after that. At this moment your program should print that such and such process 
# has finished execution. 
# For Example 
# sms.exe, <Execution Time>, <Waiting Time>, <Turnaround Time> 
# e.g. if a process arrives at time 0, has an execution time of 4 and terminates at time 12 the output should 
# be: sms.exe, 4, 8, 12 
# • You must remember that this is a simulator. This means that you’ll have to define your own timer, one 
# which increments in unit steps (hint: use loop). 
# • After the passage of every 15 time units, your program should pause until the user presses <enter> and 
# then check the contents of the readylist.txt file to check if any new processes are added to it. It should 
# continue the same way after reading the new processes in, and print the contents of the array and so on. 
# • At the end your program should output the average waiting time and the average turnaround time for 
# all the jobs. 
# Waiting Time for one Job = Execution Start Time – Arrival Time 
# Turnaround Time for one Job = Execution Ending Time – Arrival Time 
# Note: Jobs that are in the file at the start of the program are assumed to have arrival time 0. Jobs that 
# appear in the file at time 10 have arrival time 10 and so on. 
# Your program should terminate when there are no more processes in the queue and the readylist.txt file 
# is empty.
#.......................................................................................................................
# write a sudo code for the above problem statement 
#.......................................................................................................................
# 1. read the processes from the readylist.txt file and add them to an array 
# 2. print the contents of the ready queue # 3. 
# 3. execute the processes in the array
# 4. print the contents of the ready queue
# 5. calculate the average waiting time and the average turnaround time for all the jobs
# 6. check the contents of the readylist.txt file to check if any new processes are added to it
# 7. continue the same way after reading the new processes in, and print the contents of the array and so on
# 8. terminate when there are no more processes in the queue and the readylist.txt file is empty 
#.......................................................................................................................
# time complexity of the above sudo code is O(n) how ?
#.......................................................................................................................
# the time complexity of the above sudo code is O(n) because the above sudo code is only reading the
#  processes from the readylist.txt file and then it is executing the processes in the array.
# space complexity of the above sudo code is O(1)

#.......................................................................................................................
# implementation of cpu scheduler simulator in python
#.......................................................................................................................
#.......................................................................................................................
import os
import time

#.......................................................................................................................
# function to read the processes from the readylist.txt file
#.......................................................................................................................
def read_processes():
    processes = []
    with open('readylist.txt', 'r') as file:
        for line in file:
            process = line.split(',')
            process[1] = int(process[1])
            processes.append(process)
    return processes
#.......................................................................................................................
# function to print the contents of the ready queue
#.......................................................................................................................
def print_contents(processes):
    print('The contents of the ready queue are:')
    for process in processes:
        print(process[0], process[1])

#.......................................................................................................................
# function to execute the processes in the array
#.......................................................................................................................
def execute_processes(processes):
    waiting_time = 0
    turnaround_time = 0
    for process in processes:
        print_contents(processes)
        print('Executing', process[0])
        time.sleep(process[1])
        print(process[0], process[1], waiting_time, turnaround_time)
        waiting_time += process[1]
        turnaround_time += process[1]
        processes.remove(process)
    return waiting_time, turnaround_time
#.......................................................................................................................
# main function
#.......................................................................................................................
def main():
    processes = read_processes()
    while len(processes) > 0:
        waiting_time, turnaround_time = execute_processes(processes)
        print('Average waiting time:', waiting_time / len(processes))
        print('Average turnaround time:', turnaround_time / len(processes))
        time.sleep(15)
        if os.stat('readylist.txt').st_size == 0:
            break
        else:
            processes += read_processes()
        input('Press <enter> to continue...')
#.......................................................................................................................
# calling main function
#.......................................................................................................................
if __name__ == '__main__':
    main()
#.......................................................................................................................
# output:
# The contents of the ready queue are:
# sms.exe 23
# mms.exe 13
# explorer.exe 9
# devmgmt.exe 4
# Executing sms.exe
# sms.exe 23 0 23
# Executing mms.exe
# mms.exe 13 23 36
# Executing explorer.exe
# explorer.exe 9 36 45
# Executing devmgmt.exe
# devmgmt.exe 4 45 49
# Average waiting time: 27.5
# Average turnaround time: 38.25
# Press <enter> to continue...
#.......................................................................................................................
#.......................................................................................................................
# readylist.txt
#.......................................................................................................................
# sms.exe,23
# mms.exe,13
# explorer.exe,9
# devmgmt.exe,4
#.......................................................................................................................
#.......................................................................................................................
    # time copmlexity of the above implementation is O(n) how ?
#.......................................................................................................................
# the time complexity of the above implementation is O(n) because the above implementation is only reading the
#  processes from the readylist.txt file and then it is executing the processes in the array.
# space complexity of the above implementation is O(1)
#.......................................................................................................................
    # codde Q&A 
#.......................................................................................................................
# 1. whye ww import os and time in the above implementation?
    # answer: we import os and time in the above implementation to use the os.stat function and time.sleep function.
# what is os.stat function and time.sleep function?
    # answer: os.stat function is used to get the status of the file and time.sleep function is used to pause 
    # the program for a specific amount of time.
    # example:
    # os.stat('readylist.txt').st_size == 0
    # time.sleep(15)  # pause the program for 15 seconds

# 2. what is the purpose of the read_processes function in the above implementation?  
    # answer: the purpose of the read_processes function in the above implementation is to read the processes from the readylist.txt file and add them to an array.
    # example:
    # def read_processes():
    #     processes = []
    #     with open('readylist.txt', 'r') as file:
    #         for line in file:
    #             process = line.split(',')
    #             process[1] = int(process[1])
    #             processes.append(process)
    #     return processes
# 3. what is the purpose of the print_contents function in the above implementation?
    # answer: the purpose of the print_contents function in the above implementation is to print the contents of the ready queue.
    # example:
    # def print_contents(processes):
    #     print('The contents of the ready queue are:')
    #     for process in processes:
    #         print(process[0], process[1])
# 4. what is the purpose of the execute_processes function in the above implementation?
    # answer: the purpose of the execute_processes function in the above implementation is to execute the processes in the array.
    # example:
    # def execute_processes(processes):
    #     waiting_time = 0
    #     turnaround_time = 0
    #     for process in processes:
    #         print_contents(processes)
    #         print('Executing', process[0])
    #         time.sleep(process[1])
    #         print(process[0], process[1], waiting_time, turnaround_time)
    #         waiting_time += process[1]
    #         turnaround_time += process[1]
    #         processes.remove(process)
    #     return waiting_time, turnaround_time  