def print_matrix(matrix, title="Matrix:"):
    """
    Mencetak matriks ke konsol dengan format yang rapi.
    """
    print(title)
    if not matrix:
        print("[]")
        return
    for row in matrix:
        # Menggunakan f-string untuk format yang lebih baik
        print(f"  [ {'  '.join(map(str, row))} ]")