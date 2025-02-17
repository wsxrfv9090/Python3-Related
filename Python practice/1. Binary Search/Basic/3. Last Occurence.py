# Given a target integer T and an integer array A sorted in ascending order, find the index of the last occurrence of T in A or return -1 if there is no such index.

# Assumptions

# There can be duplicate elements in the array.

# Examples

# A = {1, 2, 3}, T = 2, return 1
# A = {1, 2, 3}, T = 4, return -1
# A = {1, 2, 2, 2, 3}, T = 2, return 3
# Corner Cases

# What if A is null or A is array of zero length? We should return -1 in this case.

def checkAvalability(arr, T):
    if arr == None or len(arr) == 0:
        print("Array is empty or None value")
        return False
    return True

