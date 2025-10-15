from .operations import properties

class Matrix:
    """
    Kelas untuk merepresentasikan objek matriks.
    """
    def __init__(self, data):
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            raise TypeError("Data harus berupa list of lists.")
        
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

        if not all(len(row) == self.cols for row in data):
            raise ValueError("Semua baris harus memiliki jumlah kolom yang sama.")

    def __repr__(self):
        """
        Memberikan representasi string yang rapi saat objek di-print.
        """
        if not self.data:
            return "Matrix([])"
        
        # Menggabungkan semua baris menjadi satu string dengan format yang baik
        header = "Matrix([\n"
        rows_str = ",\n".join([f"    {row}" for row in self.data])
        footer = "\n])"
        return header + rows_str + footer
    
    @property
    def shape(self):
        """
        Mengembalikan dimensi matriks sebagai tuple (baris, kolom).
        Contoh penggunaan: print(matriks.shape)
        """
        return (self.rows, self.cols)

    def transpose(self):
        """
        Mengembalikan objek Matrix baru yang merupakan hasil transpose.
        """
        # Memanggil fungsi dari modul lain
        transposed_data = properties.transpose(self.data)
        # Mengembalikan hasilnya sebagai objek Matrix baru
        return Matrix(transposed_data)