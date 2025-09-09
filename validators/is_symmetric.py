from ..matrix import Matrix

def is_symmetric(matrix):
    """
    Memeriksa apakah sebuah matriks adalah matriks simetris.
    """
    # 1. Periksa apakah matriks adalah matriks persegi
    if matrix.rows != matrix.cols:
        return False

    # 2. Periksa apakah elemen (i, j) sama dengan elemen (j, i)
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            if matrix.data[i][j] != matrix.data[j][i]:
                return False

    # 3. Jika semua elemen sesuai, matriks adalah simetris
    return True
