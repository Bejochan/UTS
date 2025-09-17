import json

def export_to_json(matrix, filename):
 """
 Mengekspor data matriks ke file JSON.
 """
 try:
  json_data = matrix.data
  json_string = json.dumps(json_data, indent=4)
  with open(filename, 'w') as file:
   file.write(json_string)
  print(f"Data matriks berhasil diekspor ke {filename}")

 except Exception as e:
  print(f"Terjadi kesalahan saat mengekspor data: {e}")
