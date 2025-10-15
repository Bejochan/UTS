# 📱 Aplikasi Prediksi Penggunaan HP

Aplikasi web berbasis Flask yang menggunakan Machine Learning (Regresi Linier Berganda) untuk memprediksi waktu penggunaan HP berdasarkan jam tidur dan aktivitas harian.

## ✨ Fitur Utama

- 🎯 **Prediksi Real-time** - Langsung mendapat hasil prediksi
- 📊 **Visualisasi Data** - Scatter plot data training interaktif
- 🎨 **UI Modern** - Desain gradient yang menarik dan responsive
- 📈 **Informasi Model** - Melihat persamaan regresi dan akurasi
- 💡 **Rekomendasi Pintar** - Saran berdasarkan hasil prediksi
- 📉 **Statistik Detail** - Persentase penggunaan HP dan sisa waktu produktif

## 🚀 Cara Instalasi

### 1. Clone atau Download Project

```bash
# Buat folder project
mkdir prediksi-hp
cd prediksi-hp
```

### 2. Buat Struktur Folder

```
prediksi-hp/
│
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

### 3. Install Dependencies

```bash
# Install semua package yang dibutuhkan
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi

```bash
python app.py
```

### 5. Buka di Browser

Akses aplikasi di: **http://127.0.0.1:5000**

## 🎮 Cara Menggunakan

1. **Geser Slider** untuk mengatur jam tidur (3-12 jam)
2. **Geser Slider** untuk mengatur jam aktivitas (0-16 jam)
3. **Klik "Prediksi Sekarang"** untuk mendapat hasil
4. **Lihat Hasil** berupa:
   - Estimasi jam penggunaan HP
   - Kategori (Sangat Rendah, Rendah, Sedang, Tinggi, Sangat Tinggi)
   - Rekomendasi personal
   - Sisa waktu produktif
   - Persentase waktu di HP

## 📐 Algoritma yang Digunakan

### Regresi Linier Berganda

Formula: **HP = β₀ + β₁(Tidur) + β₂(Aktivitas)**

- Menggunakan **Normal Equation**: θ = (X^T X)^(-1) X^T y
- Implementasi **tanpa library ML** (numpy saja)
- Dataset training: **500 data realistis**

### Logika Dataset

- Semakin **sedikit tidur** → Lebih banyak main HP
- Semakin **banyak aktivitas** → Lebih sedikit waktu untuk HP
- Formula: `HP ≈ 18 - Tidur - Aktivitas + noise`

## 🎯 Kategori Penggunaan HP

| Jam HP | Kategori | Status |
|--------|----------|--------|
| < 4 jam | Sangat Rendah | 🟢 Sangat Sehat |
| 4-6 jam | Rendah | 🟢 Sehat |
| 6-8 jam | Sedang | 🟡 Cukup |
| 8-10 jam | Tinggi | 🟠 Perhatian |
| > 10 jam | Sangat Tinggi | 🔴 Bahaya |

## 📊 API Endpoints

### 1. GET `/`
- Halaman utama aplikasi

### 2. POST `/predict`
- **Body**: `{"tidur": 7, "aktivitas": 8}`
- **Response**: 
```json
{
  "prediksi": 5.23,
  "kategori": "Rendah 🟢",
  "rekomendasi": "Bagus! Pertahankan pola penggunaan HP yang sehat."
}
```

### 3. GET `/model-info`
- Informasi koefisien model dan R² score

### 4. GET `/dataset`
- 100 data pertama dari dataset training

## 🛠️ Teknologi yang Digunakan

- **Backend**: Flask (Python)
- **Machine Learning**: NumPy (Manual Implementation)
- **Frontend**: HTML5, CSS3, JavaScript
- **Visualisasi**: Chart.js
- **Design**: Gradient UI dengan animasi

## 🔧 Troubleshooting

### Error: "Module not found"
```bash
pip install -r requirements.txt --upgrade
```

### Error: "Port already in use"
```bash
# Ubah port di app.py, baris terakhir:
app.run(debug=True, port=5001)
```

### Error: "Template not found"
Pastikan struktur folder benar:
```
prediksi-hp/
├── app.py
└── templates/
    └── index.html
```

## 📈 Contoh Penggunaan

### Contoh 1: Mahasiswa Aktif
- **Input**: Tidur 6 jam, Aktivitas 10 jam
- **Output**: HP ~6-7 jam (Sedang 🟡)
- **Rekomendasi**: Cukup baik, tapi bisa dikurangi

### Contoh 2: Pekerja Sibuk
- **Input**: Tidur 7 jam, Aktivitas 9 jam
- **Output**: HP ~4-5 jam (Rendah 🟢)
- **Rekomendasi**: Bagus! Pertahankan pola yang sehat

### Contoh 3: Liburan
- **Input**: Tidur 9 jam, Aktivitas 3 jam
- **Output**: HP ~9-10 jam (Tinggi 🟠)
- **Rekomendasi**: Perhatian! Kurangi screen time

## 🎨 Kustomisasi

### Mengubah Warna Tema
Edit di `templates/index.html`, bagian `<style>`:
```css
/* Ubah gradient utama */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Menjadi warna lain, misal hijau-biru */
background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
```

### Menambah Dataset
Edit di `app.py`:
```python
# Ubah jumlah data training
n_samples = 1000  # dari 500 menjadi 1000
```

### Mengubah Range Input
Edit di `templates/index.html`:
```html
<!-- Ubah range tidur -->
<input type="range" id="tidur" min="3" max="15" value="7">
```

## 📚 Penjelasan Kode

### 1. Class LinearRegression
```python
class LinearRegression:
    def fit(self, X, y):
        # Implementasi Normal Equation
        # θ = (X^T X)^(-1) X^T y
```
- Melatih model tanpa library ML eksternal
- Menggunakan operasi matriks NumPy
- Menghitung intercept dan coefficients

### 2. Generate Dataset
```python
# Data mengikuti distribusi realistis
tidur_jam = np.random.choice([4,5,6,7,8,9], ...)
aktivitas_jam = np.random.choice([3,4,5,6,7,8,9,10], ...)
hp_jam = 18 - tidur_jam - aktivitas_jam + noise
```

### 3. API Prediction
```python
@app.route('/predict', methods=['POST'])
def predict():
    # Terima input
    # Validasi
    # Prediksi
    # Return hasil + kategori + rekomendasi
```

## 🎓 Konsep Machine Learning

### Normal Equation
**θ = (X^T X)^(-1) X^T y**

Dimana:
- θ = Parameter model (coefficients)
- X = Matriks fitur
- y = Target variable
- X^T = Transpose dari X

### R² Score (Coefficient of Determination)
**R² = 1 - (SS_res / SS_tot)**

- **SS_res**: Sum of Squared Residuals
- **SS_tot**: Total Sum of Squares
- **Range**: 0 - 1 (semakin tinggi semakin baik)
- **Interpretasi**: 
  - R² = 0.8 → Model menjelaskan 80% variasi data
  - R² = 0.5 → Model menjelaskan 50% variasi data

## 📝 Catatan Penting

1. **Validasi Input**: Aplikasi memvalidasi input untuk mencegah nilai tidak realistis
2. **Batasan Output**: Hasil prediksi dibatasi antara 0-16 jam
3. **Dataset Realistis**: Data training mengikuti pola perilaku nyata
4. **Responsif**: UI otomatis menyesuaikan dengan ukuran layar

## 🚀 Pengembangan Lebih Lanjut

### Fitur yang Bisa Ditambahkan:
1. ✅ **Export Hasil** - Download hasil prediksi sebagai PDF
2. ✅ **History** - Simpan riwayat prediksi pengguna
3. ✅ **Multiple Models** - Bandingkan dengan model ML lain
4. ✅ **User Authentication** - Login untuk tracking jangka panjang
5. ✅ **Data Upload** - Upload dataset custom
6. ✅ **Visualisasi 3D** - Plot 3D untuk melihat hubungan variabel
7. ✅ **Mobile App** - Konversi ke aplikasi mobile

### Algoritma Alternatif:
- Decision Tree Regression
- Random Forest
- Support Vector Regression (SVR)
- Neural Networks

## 📞 Support

Jika ada pertanyaan atau masalah:
1. Periksa struktur folder
2. Pastikan semua dependencies terinstall
3. Cek versi Python (minimal 3.8)
4. Periksa console untuk error messages

## 📄 Lisensi

Project ini dibuat untuk keperluan edukasi dan pembelajaran Machine Learning.

## 👨‍💻 Developer

Dibuat dengan ❤️ menggunakan:
- Python + Flask
- NumPy untuk operasi matriks
- Chart.js untuk visualisasi
- CSS3 untuk animasi modern

---

**Happy Coding! 🚀**

Jangan lupa untuk:
- ⭐ Star project ini jika bermanfaat
- 🐛 Report bugs jika menemukan error
- 💡 Suggest fitur baru untuk pengembangan