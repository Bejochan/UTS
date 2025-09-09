from ..matrix import Matrix

def is_identity(matrix):
    """
    Memeriksa apakah sebuah matriks adalah matriks identitas.
    """
    # 1. Periksa apakah matriks adalah matriks persegi
    if matrix.rows != matrix.cols:
        return False

    # 2. Periksa elemen-elemen matriks
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            # Periksa elemen diagonal
            if i == j:
                if matrix.data[i][j] != 1:
                    return False
            # Periksa elemen non-diagonal
            else:
                if matrix.data[i][j] != 0:
                    return False

    # 3. Jika semua elemen sesuai, matriks adalah identitas
    return True
