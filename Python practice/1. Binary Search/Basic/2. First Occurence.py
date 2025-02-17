# Given a target integer T and an integer array A sorted in ascending order, find the index of the first occurrence of T in A or return -1 if there is no such index.

# Assumptions

# There can be duplicate elements in the array.
# Examples

# A = {1, 2, 3}, T = 2, return 1
# A = {1, 2, 3}, T = 4, return -1
# A = {1, 2, 2, 2, 3}, T = 2, return 1
# Corner Cases

# What if A is null or A of zero length? We should return -1 in this case.

def checkAvalability(arr, T):
    if arr == None or len(arr) == 0:
        print("Array is empty or None value")
        return False
    return True
    

def biSearch(arr, T):
    if checkAvalability(arr, T):
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < T:
                left = mid + 1
            elif arr[mid] >= T:
                right = mid
        if left == right and arr[left] == T:
            return left
        elif left == right and arr[left] != T:
            return -1
    else:
        return -1


# Testing
import random
random_array = [random.randint(0, 13) for _ in range(10)]
random_array.sort()
print("Array content: " + str(random_array))
T= random.randint(0, 13)
print("T: " + str(T))
print(biSearch(random_array, T))