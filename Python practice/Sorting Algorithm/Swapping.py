

# Swapping using XOR operator
def swap(a, b):
    a = a ^ b
    b = a ^ b  # now b is equal to original a
    a = a ^ b  # now a is equal to original b
    return a, b