class SparseMatrix:
    """
    Kelas untuk merepresentasikan matriks jarang (sparse matrix)
    menggunakan metode Dictionary of Keys (DOK).
    """
    def __init__(self, rows, cols):
        """
        Inisialisasi matriks dengan dimensi, bukan dengan data penuh.
        """
        if rows <= 0 or cols <= 0:
            raise ValueError("Dimensi matriks harus positif.")
        self.rows = rows
        self.cols = cols
        self._data = {}  # Dictionary untuk menyimpan elemen tidak nol

    @property
    def shape(self):
        """Mengembalikan dimensi matriks sebagai tuple (baris, kolom)."""
        return (self.rows, self.cols)

    def __getitem__(self, key):
        """
        Mengambil nilai pada posisi (baris, kolom).
        Memungkinkan akses seperti: matriks[baris, kolom]
        """
        row, col = key
        # Jika posisi ada di dictionary, kembalikan nilainya. Jika tidak, berarti nilainya 0.
        return self._data.get((row, col), 0)

    def __setitem__(self, key, value):
        """
        Menetapkan nilai pada posisi (baris, kolom).
        Memungkinkan penetapan seperti: matriks[baris, kolom] = nilai
        """
        row, col = key
        # Validasi apakah posisi valid
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("Indeks matriks di luar jangkauan.")
        
        if value != 0:
            # Hanya simpan jika nilainya tidak nol
            self._data[(row, col)] = value
        elif (row, col) in self._data:
            # Jika nilai diubah menjadi 0, hapus dari dictionary
            del self._data[(row, col)]

    def __repr__(self):
        """Representasi string untuk menampilkan informasi matriks."""
        return f"SparseMatrix(shape=({self.rows}, {self.cols}), non_zero_elements={len(self._data)})"

    def to_dense(self):
        """
        Mengubah representasi sparse menjadi matriks padat (list of lists).
        Berguna untuk visualisasi atau operasi yang butuh matriks penuh.
        """
        # Buat matriks penuh berisi nol
        dense_matrix = [[0] * self.cols for _ in range(self.rows)]
        # Isi dengan nilai tidak nol dari dictionary
        for (row, col), value in self._data.items():
            dense_matrix[row][col] = value
        return dense_matrix

    def __add__(self, other):
        """
        Menambahkan dua sparse matrix.
        """
        if self.shape != other.shape:
            raise ValueError("Matriks harus memiliki dimensi yang sama untuk dijumlahkan.")

        new_matrix = SparseMatrix(self.rows, self.cols)
        
        # Salin semua data dari matriks pertama
        new_matrix._data = self._data.copy()

        # Tambahkan data dari matriks kedua
        for (row, col), value in other._data.items():
            # Menggunakan __setitem__ dan __getitem__ dari kelas ini sendiri
            new_matrix[row, col] += value
            
        return new_matrix