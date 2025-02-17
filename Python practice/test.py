
#Custom Case
arr_t = [3, 4, 5, 6, 6, 9, 16]
T_t = 5

def checkAvailability(arr, T):
    if len(arr_t) == 0 or arr_t == NULL:
        return True
    else:
        return False

def biSearch(arr, T):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if T == arr[mid]:
            return mid
        elif T > arr[mid]:
            left = mid + 1
        elif T < arr[mid]:
            right = mid - 1
        else:
            return -1

if checkAvailability(arr_t, T_t):
    print(f"Index of T in Array: {('Found at index: ' + str(biSearch(arr_t, T_t)) + '.\n') if biSearch(arr_t, T_t) != -1 else 'Wasn't able to find given numbers.\n'}")
else:
    print("Assigning space for array or length is 0.\n")