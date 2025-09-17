import time
from matriks import Matrix
from operations.adder import add_matrices
from operations.multiplier import multiply_matrices
from utilities import print_matrix
from exporters.csv_exporter import export_to_csv
from sparsematrix import SparseMatrix

def create_sparse_data(size):
 data = [[0] * size for _ in range(size)]
 data[0][0] = 1
 data[size-1][size-1] = 1
 return data

if __name__ == "__main__":
 matriks_a = Matrix([[1, 2], [3, 4]])
 matriks_b = Matrix([[5, 6], [7, 8]])
 print("Hasil Penjumlahan:")
 hasil_penjumlahan = add_matrices(matriks_a, matriks_b)
 print_matrix(hasil_penjumlahan)
 print("\nHasil Perkalian:")
 hasil_perkalian = multiply_matrices(matriks_a, matriks_b)
 print_matrix(hasil_perkalian)
 matrix_c = Matrix([[10, 20], [30, 40]])
 print("\nMenyimpan Matriks C ke file CSV:")
 export_to_csv(matrix_c, "matriks_c.csv")
 print("\n--- Menguji Masalah Performa ---")
 sparse_data_1000 = create_sparse_data(1000)
 mat_a = Matrix(sparse_data_1000)
 mat_b = Matrix(sparse_data_1000)
 start_time = time.time()
 product_mat = multiply_matrices(mat_a, mat_b)
 end_time = time.time()
 print(f"Waktu yang dibutuhkan untuk perkalian: {end_time - start_time:.2f} detik")
 print("\n--- Menguji Solusi dengan SparseMatrix ---")
 sparse_data_1000 = create_sparse_data(1000)
 
 # Perhatikan: kita instansiasi SparseMatrix
 mat_a = SparseMatrix(sparse_data_1000)
 mat_b = SparseMatrix(sparse_data_1000)
 
 start_time = time.time()
 # Perhatikan: fungsi multiply_matrices() tidak berubah sama sekali
 product_mat = multiply_matrices(mat_a, mat_b)
 end_time = time.time()
 print(f"Waktu yang dibutuhkan untuk perkalian: {end_time - start_time:.2f} detik")
