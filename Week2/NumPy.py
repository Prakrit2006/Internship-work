import numpy as np
# One Dimensional array
arr = np.array([10, 20, 30, 40, 50])
print(arr)
# Two dimensional array
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(arr2)
# Three dimensional array
arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(arr3)

#Matrix addition

A=np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
B=np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
C=A+B
print(C)
D=np.add(A,B)
print(D)

# Matrix Multiplication

# First matrix (2 × 3)
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Second matrix (3 × 2)
B = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

# Matrix multiplication
C = A @ B
print("\nProduct of matrices:")
print(C)
#Mean & Std in NumPy

arr = np.array([10, 20, 30, 40, 50,60])
mean = np.mean(arr)
std = np.std(arr)
print("Array:", arr)
print("Mean:", mean)
print("Standard Deviation:", std)
#Reshape Array
new_arr = arr.reshape(2, 3)
print("Original Array:")
print(arr)
print("\nReshaped Array:")
print(new_arr)