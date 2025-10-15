# 🚀 Quick Start Guide - Aplikasi Prediksi HP

## 📁 Struktur Folder Yang Benar

```
prediksi-hp/
│
├── app.py                    # Versi basic
├── app_enhanced.py           # Versi lengkap (RECOMMENDED)
├── requirements.txt
├── README.md
├── QUICK_START.md
│
└── templates/
    ├── index.html           # Versi basic
    └── index_enhanced.html  # Versi lengkap (RECOMMENDED)
```

## ⚡ Instalasi Super Cepat (3 Langkah)

### 1️⃣ Buat Folder Project
```bash
mkdir prediksi-hp
cd prediksi-hp
```

### 2️⃣ Copy Semua File
- Copy `app_enhanced.py` → Rename jadi `app.py`
- Copy `requirements.txt`
- Buat folder `templates/`
- Copy `index_enhanced.html` → Simpan di `templates/` dengan nama `index.html`

### 3️⃣ Install & Run
```bash
pip install -r requirements.txt
python app.py
```

✅ **DONE!** Buka browser: http://127.0.0.1:5000

---

## 🎯 Fitur Aplikasi

### 🔮 Tab 1: Prediksi
- **Slider Input** untuk Jam Tidur (3-12 jam)
- **Slider Input** untuk Jam Aktivitas (0-16 jam)
- **Prediksi Real-time** dengan kategori warna:
  - 🟢 Sangat Rendah/Rendah (< 6 jam)
  - 🟡 Sedang (6-8 jam)
  - 🟠 Tinggi (8-10 jam)
  - 🔴 Sangat Tinggi (> 10 jam)
- **Rekomendasi Personal** berdasarkan hasil
- **Visualisasi Scatter Plot** data training
- **Informasi Model** (Persamaan, R², MSE, MAE)

### 📜 Tab 2: History
- **Tabel Riwayat** semua prediksi yang pernah dilakukan
- **Timestamp** setiap prediksi
- **Export ke CSV** untuk analisis lebih lanjut

### 📊 Tab 3: Statistik
- **Statistik Dataset Lengkap**:
  - Min, Max, Mean, Std Dev untuk setiap variabel
- **Performa Model**:
  - R² Score (Akurasi)
  - MSE (Mean Squared Error)
  - MAE (Mean Absolute Error)
- **Chart Distribusi** data
- **Export Dataset** ke CSV

---

## 🎨 Preview Fitur

### 1. Prediksi dengan Animasi
```
Input: Tidur 7 jam, Aktivitas 8 jam
Output: HP ~5.2 jam (Rendah 🟢)
Rekomendasi: "Bagus! Pertahankan pola yang sehat!"
```

### 2. History Tracking
```
| Waktu              | Tidur | Aktivitas | HP   | Kategori |
|--------------------|-------|-----------|------|----------|
| 2025-01-15 10:30   | 7     | 8         | 5.2  | Rendah   |
| 2025-01-15 10:25   | 6     | 10        | 6.8  | Sedang   |
```

### 3. Export Data
- **Export History**: Download semua prediksi sebagai CSV
- **Export Dataset**: Download data training (500 data)

---

## 🔧 Troubleshooting

### ❌ Error: "No module named 'flask'"
```bash
pip install Flask numpy
```

### ❌ Error: "Template not found"
Pastikan struktur folder:
```
prediksi-hp/
├── app.py
└── templates/
    └── index.html    ← HARUS di dalam folder templates!
```

### ❌ Port 5000 sudah dipakai
Edit `app.py` baris terakhir:
```python
app.run(debug=True, port=5001)  # Ganti ke port lain
```

### ❌ Tombol tidak bisa diklik
- Pastikan pakai **app_enhanced.py** (bukan app.py basic)
- Pastikan pakai **index_enhanced.html** (bukan index.html basic)

---
