# NumPy program to perform matrix operations.

import numpy as np

# Creating matrices
matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

# Matrix addition
addition = matrix1 + matrix2

# Matrix subtraction
subtraction = matrix1 - matrix2

# Matrix multiplication
multiplication = np.dot(matrix1, matrix2)

# Matrix inverse
inverse_matrix1 = np.linalg.inv(matrix1)

# Displaying results
print("Matrix 1:\n", matrix1)

print("\nMatrix 2:\n", matrix2)

print("\nAddition:\n", addition)

print("\nSubtraction:\n", subtraction)

print("\nMultiplication:\n", multiplication)

print("\nInverse of Matrix 1:\n", inverse_matrix1)

# Expected Output
"""
Addition:
[[ 6  8]
 [10 12]]

Subtraction:
[[-4 -4]
 [-4 -4]]

Multiplication:
[[19 22]
 [43 50]]
"""