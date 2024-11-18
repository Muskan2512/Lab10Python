import numpy as np

# Define matrices
A = np.array([[2, -1], [-1, 2]])
B = np.array([[1, 2], [3, 4]])
C = np.array([[0, 3], [-3, 0]])
D = np.array([[3, complex(1,-1)], [complex(1,1), -2]])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)

# (a) Add, subtract, multiply, and divide 2 matrices
print("\nAddition of A and B:\n", A + B)
print("\nSubtraction of A and B:\n", A - B)
print("\nMultiplication of A and B:\n", np.dot(A, B))
try:
    print("\nDivision of A and B (element-wise):\n", A / B)
except ZeroDivisionError:
    print("\nDivision not possible (division by zero).")

# (b) Determinant of matrices
# np.linalg is a submodule in the NumPy library that provides a collection of linear algebra functions

# np.linalg.inv: Computes the inverse of a matrix.
# np.linalg.det: Computes the determinant of a matrix.
# np.linalg.matrix_rank: Computes the rank of a matrix.
# np.linalg.solve: Solves a linear system of equations 
# 𝐴
# 𝑥
# =
# 𝐵
# Ax=B.
det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
print("\nDeterminant of A:", det_A)
print("Determinant of B:", det_B)

# (c) Check if matrices are symmetric

# np.allclose(matrix, matrix.T):Returns True if two arrays are element-wise equal within a tolerance.
# symmetric A=A transpose
def is_symmetric(matrix):
    return np.allclose(matrix, matrix.T)

print("\nIs A symmetric?", is_symmetric(A))
print("Is B symmetric?", is_symmetric(B))

# (d) Check if matrices are skew-symmetric
def is_skew_symmetric(matrix):
    return np.allclose(matrix, -matrix.T)

print("\nIs A skew-symmetric?", is_skew_symmetric(A))
print("Is B skew-symmetric?", is_skew_symmetric(B))
print("Is B skew-symmetric?", is_skew_symmetric(C))

# (e) Check if matrices are Hermitian
def is_hermitian(matrix):
    return np.allclose(matrix, np.conj(matrix.T))

print("\nIs A Hermitian?", is_hermitian(A))
print("\nIs D Hermitian?", is_hermitian(D))
print("Is B Hermitian?", is_hermitian(B))

# (f) Check if matrices are skew-Hermitian
def is_skew_hermitian(matrix):
    return np.allclose(matrix, -np.conj(matrix.T))

print("\nIs A skew-Hermitian?", is_skew_hermitian(A))
print("Is B skew-Hermitian?", is_skew_hermitian(B))

# (g) Check if matrices are orthogonal
# matrix.shape[0]- returns the number of rows in matrix
def is_orthogonal(matrix):
    return np.allclose(np.dot(matrix, matrix.T), np.eye(matrix.shape[0]))

print("\nIs A orthogonal?", is_orthogonal(A))
print("Is B orthogonal?", is_orthogonal(B))

# (h) Check if matrices are upper or lower triangular
def is_upper_triangular(matrix):
    return np.allclose(matrix, np.triu(matrix))

def is_lower_triangular(matrix):
    return np.allclose(matrix, np.tril(matrix))

print("\nIs A upper triangular?", is_upper_triangular(A))
print("Is A lower triangular?", is_lower_triangular(A))
print("\nIs B upper triangular?", is_upper_triangular(B))
print("Is B lower triangular?", is_lower_triangular(B))

# (i) Adjoint of the matrices
# adjoint_A = np.conjugate(A.T)
# adjoint_B = np.conjugate(B.T)
# print("\nAdjoint of A:\n", adjoint_A)
# print("\nAdjoint of B:\n", adjoint_B)
