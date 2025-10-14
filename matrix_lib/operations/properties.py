import numpy as np

def determinant(matrix):
    """Menghitung determinan dari sebuah matriks secara rekursif."""
    # Pengecekan: matriks harus persegi
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matriks harus persegi untuk menghitung determinan.")
    
    # Kasus dasar untuk matriks 2x2
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    # Rekursi dengan ekspansi kofaktor sepanjang baris pertama
    for c in range(len(matrix)):
        minor = get_minor(matrix, 0, c)
        # Tanda + atau - tergantung pada posisi kolom
        sign = (-1) ** c
        det += sign * matrix[0][c] * determinant(minor)
        
    return det

def transpose(matrix):
    """Menghitung transpose dari sebuah matriks."""
    if not matrix or not matrix[0]:
        return []
    return [list(row) for row in zip(*matrix)]

def get_minor(matrix, r, c):
    """Mendapatkan minor dari sebuah matriks dengan menghapus baris r dan kolom c."""
    return [row[:c] + row[c+1:] for row in (matrix[:r] + matrix[r+1:])]

def inverse(matrix):
    """Menghitung invers dari sebuah matriks n x n."""
    # Pengecekan awal
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matriks harus persegi untuk bisa diinvers.")
    
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Determinan adalah 0, matriks ini tidak memiliki invers.")
    
    # Kasus khusus untuk matriks 2x2 (lebih cepat)
    if len(matrix) == 2:
        return [
            [matrix[1][1]/det, -matrix[0][1]/det],
            [-matrix[1][0]/det, matrix[0][0]/det]
        ]
        
    # Membuat matriks kofaktor
    cofactors = []
    for r in range(len(matrix)):
        cofactor_row = []
        for c in range(len(matrix)):
            minor = get_minor(matrix, r, c)
            sign = (-1) ** (r + c)
            cofactor_row.append(sign * determinant(minor))
        cofactors.append(cofactor_row)
        
    # Membuat matriks adjugate (transpose dari matriks kofaktor)
    adjugate = transpose(cofactors)
    
    # Langkah terakhir: bagi setiap elemen adjugate dengan determinan
    inverse_matrix = []
    for r in range(len(adjugate)):
        row = []
        for c in range(len(adjugate[0])):
            row.append(adjugate[r][c] / det)
        inverse_matrix.append(row)
        
    return inverse_matrix