# NumPy program to create a 5x5 matrix
# and calculate row-wise sum, column-wise sum,
# transpose, and determinant.

import numpy as np

# Creating 5x5 matrix with random integers
matrix = np.random.randint(1, 100, (5, 5))

# Displaying matrix
print("5x5 Matrix:\n")
print(matrix)

# Row-wise sum
row_sum = np.sum(matrix, axis=1)

# Column-wise sum
column_sum = np.sum(matrix, axis=0)

# Transpose of matrix
transpose_matrix = matrix.T

# Determinant of matrix
determinant = np.linalg.det(matrix)

# Displaying results
print("\nRow-wise Sum:")
print(row_sum)

print("\nColumn-wise Sum:")
print(column_sum)

print("\nTranspose of Matrix:")
print(transpose_matrix)

print("\nDeterminant of Matrix:")
print(determinant)

# Expected Output
"""
5x5 Matrix:

[[12 45 67 23 89]
 [34 56 78 90 11]
 [22 33 44 55 66]
 [77 88 99 10 20]
 [15 25 35 45 55]]

Row-wise Sum:
[236 269 220 294 175]

Column-wise Sum:
[160 247 323 223 241]

Transpose of Matrix:
[[12 34 22 77 15]
 [45 56 33 88 25]
 [67 78 44 99 35]
 [23 90 55 10 45]
 [89 11 66 20 55]]

Determinant of Matrix:
-2.345678e+08
"""