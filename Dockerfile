# 1. Mulai dari fondasi Python
FROM python:3.9-alpine

# 2. Tetapkan direktori kerja di dalam container
WORKDIR /app

# 3. Salin file requirements.txt terlebih dahulu
COPY requirements.txt .

# 4. Instal semua pustaka yang dibutuhkan
RUN pip install -r requirements.txt

# 5. Salin semua file proyek lainnya
COPY . .

# 6. Beri tahu Docker port yang akan digunakan oleh Flask
EXPOSE 5000

# 7. Perintah untuk menjalankan aplikasi Flask saat container dimulai
CMD ["python", "app.py"]