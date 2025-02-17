# Given a target integer T and an integer array A sorted in ascending order, find the index i such that A[i] == T or return -1 if there is no such index.

# Assumptions

# There can be duplicate elements in the array, and you can return any of the indices i such that A[i] == T.
# Examples

# A = {1, 2, 3, 4, 5}, T = 3, return 2
# A = {1, 2, 3, 4, 5}, T = 6, return -1
# A = {1, 2, 2, 2, 3, 4}, T = 2, return 1 or 2 or 3
# Corner Cases

# What if A is null or A is of zero length? We should return -1 in this case.


# Outline:
# 1. Choosing Fibonacci array as the search space
# 2. Generate a random T value
# 3. Range (0, 1000) for the array
# 4. Generate a random T value (range 0, 1000)
# 5. Function generating an array of Fibonacci numbers
# 6. Function to find the index of T in the array

#Solution:

#0.
#Defining the size
size = 10

#1.
#Functions for generating Fibonacci numbers based on a index parameter
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
#2. 
#Function to generate a random T value
import random
T = random.randint(0, fibonacci(size))
print('Random T value:', T)

#3.
#Function to generate Fibonacci array
import numpy as np
def fibonacci_array(sz):
    fib_array = []
    for i in range(sz):
        fib_array.append(fibonacci(i))
    return np.array(fib_array)


# Initialize arrays as numpy arrays
A = np.array([1, 2, 3, 4, 5])
T_A = 3
B = np.array([1, 2, 3, 4, 5])
T_B = 6
C = np.array([1, 2, 2, 2, 3, 4])
T_C = 2

# Store arrays into one list
arrays_list = [fibonacci_array(size), A, B, C]
print("Arrays list:\n", arrays_list)
target_list = [T, T_A, T_B, T_C]
print("Arrays list:\n", target_list)

#4.
#Binary search function(Left most element)
def binary_search(arr, T):
    left = 0
    right = len(arr) - 1
    mid = left + (right - left) // 2
    while left <= right:
        if arr[mid] >= T:
            right = mid - 1
        elif arr[mid] < T:
            left = mid + 1
        if left == right and arr[left] == T:
            return left
        elif (left == right and arr[left] != T):
            return -1

i = 0
for i in range(len(arrays_list)):
    print("T value: ", target_list[i])
    print("Array: ", arrays_list[i])
    print(f"Index of T in Array: {('found at index ' + str(binary_search(arrays_list[i], target_list[i]))) if binary_search(arrays_list[i], target_list[i]) != -1 else 'not found'}")
    print("\n")
    i += 1
    
