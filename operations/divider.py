from ..matrix import Matrix

def divide_matrices(matrix1, matrix2):
    """
    Melakukan operasi pembagian pada dua objek matriks.
    Fungsi ini memiliki bug karena tidak melakukan validasi dimensi.
    """
    result_data = [[0 for _ in range(matrix1.cols)] for _ in range(matrix1.rows)]
    for i in range(matrix1.rows):
        for j in range(matrix1.cols):
            result_data[i][j] = matrix1.data[i][j] / matrix2.data[i][j]

    return Matrix(result_data)
