# app_enhanced.py - Versi lengkap dengan fitur export
from flask import Flask, render_template, request, jsonify, send_file
import numpy as np
import json
import csv
from datetime import datetime
from io import StringIO, BytesIO

app = Flask(__name__)

# Storage untuk history prediksi (dalam memory)
prediction_history = []

class LinearRegression:
    """Kelas untuk regresi linier berganda menggunakan matriks"""
    
    def __init__(self):
        self.coefficients = None
        self.intercept = None
        self.X_train = None
        self.y_train = None
    
    def fit(self, X, y):
        """
        Melatih model regresi linier menggunakan metode Normal Equation
        X: matriks fitur (n x m)
        y: vektor target (n x 1)
        """
        self.X_train = X
        self.y_train = y
        
        # Tambahkan kolom ones untuk intercept
        X_with_intercept = np.column_stack([np.ones(len(X)), X])
        
        # Normal Equation: θ = (X^T X)^(-1) X^T y
        X_transpose = X_with_intercept.T
        X_transpose_X = X_transpose @ X_with_intercept
        X_transpose_X_inv = np.linalg.inv(X_transpose_X)
        X_transpose_y = X_transpose @ y
        
        theta = X_transpose_X_inv @ X_transpose_y
        
        self.intercept = theta[0]
        self.coefficients = theta[1:]
        
        return self
    
    def predict(self, X):
        """Prediksi nilai target"""
        if self.coefficients is None:
            raise Exception("Model belum dilatih!")
        
        return self.intercept + np.dot(X, self.coefficients)
    
    def score(self, X, y):
        """Menghitung R-squared"""
        y_pred = self.predict(X)
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        r2 = 1 - (ss_res / ss_tot)
        return r2
    
    def mean_squared_error(self, X, y):
        """Menghitung Mean Squared Error"""
        y_pred = self.predict(X)
        mse = np.mean((y - y_pred) ** 2)
        return mse
    
    def mean_absolute_error(self, X, y):
        """Menghitung Mean Absolute Error"""
        y_pred = self.predict(X)
        mae = np.mean(np.abs(y - y_pred))
        return mae

# Generate dataset training
np.random.seed(42)
n_samples = 500

# Generate data realistis
tidur_jam = np.random.choice([4, 5, 6, 7, 8, 9], size=n_samples, p=[0.05, 0.15, 0.25, 0.30, 0.20, 0.05])
aktivitas_jam = np.random.choice([3, 4, 5, 6, 7, 8, 9, 10], size=n_samples, p=[0.05, 0.10, 0.15, 0.25, 0.25, 0.15, 0.03, 0.02])

# Formula: HP = 18 - tidur - aktivitas + noise
hp_jam = 18 - tidur_jam - aktivitas_jam + np.random.normal(0, 1, n_samples)
hp_jam = np.clip(hp_jam, 2, 12)  # Batasi antara 2-12 jam

# Buat matriks X dan vektor y
X_train = np.column_stack([tidur_jam, aktivitas_jam])
y_train = hp_jam

# Latih model
model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        tidur = float(data['tidur'])
        aktivitas = float(data['aktivitas'])
        
        # Validasi input
        if tidur < 3 or tidur > 12:
            return jsonify({'error': 'Jam tidur harus antara 3-12 jam'}), 400
        if aktivitas < 0 or aktivitas > 16:
            return jsonify({'error': 'Jam aktivitas harus antara 0-16 jam'}), 400
        
        # Prediksi
        X_pred = np.array([[tidur, aktivitas]])
        hp_pred = model.predict(X_pred)[0]
        hp_pred = max(0, min(16, hp_pred))  # Batasi hasil
        
        # Kategori
        if hp_pred < 4:
            kategori = "Sangat Rendah 🟢"
            kategori_color = "#10b981"
            rekomendasi = "Luar biasa! Penggunaan HP Anda sangat sehat. Teruskan pola hidup seimbang ini!"
        elif hp_pred < 6:
            kategori = "Rendah 🟢"
            kategori_color = "#22c55e"
            rekomendasi = "Bagus! Pertahankan pola penggunaan HP yang sehat. Anda sudah melakukan yang terbaik!"
        elif hp_pred < 8:
            kategori = "Sedang 🟡"
            kategori_color = "#eab308"
            rekomendasi = "Cukup baik, namun masih bisa dikurangi untuk kesehatan mata dan produktivitas."
        elif hp_pred < 10:
            kategori = "Tinggi 🟠"
            kategori_color = "#f97316"
            rekomendasi = "Perhatian! Kurangi screen time untuk kesehatan Anda. Cobalah aktivitas offline."
        else:
            kategori = "Sangat Tinggi 🔴"
            kategori_color = "#ef4444"
            rekomendasi = "Bahaya! Segera kurangi penggunaan HP secara signifikan. Konsultasikan dengan ahli jika perlu."
        
        # Simpan ke history
        history_entry = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'tidur': tidur,
            'aktivitas': aktivitas,
            'prediksi': round(hp_pred, 2),
            'kategori': kategori
        }
        prediction_history.append(history_entry)
        
        # Batasi history maksimal 100 entry
        if len(prediction_history) > 100:
            prediction_history.pop(0)
        
        return jsonify({
            'prediksi': round(hp_pred, 2),
            'kategori': kategori,
            'kategori_color': kategori_color,
            'rekomendasi': rekomendasi
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/model-info')
def model_info():
    """Endpoint untuk informasi model"""
    r2_score = model.score(X_train, y_train)
    mse = model.mean_squared_error(X_train, y_train)
    mae = model.mean_absolute_error(X_train, y_train)
    
    return jsonify({
        'intercept': float(model.intercept),
        'coef_tidur': float(model.coefficients[0]),
        'coef_aktivitas': float(model.coefficients[1]),
        'r2_score': float(r2_score),
        'mse': float(mse),
        'mae': float(mae),
        'n_samples': len(X_train),
        'mean_tidur': float(np.mean(X_train[:, 0])),
        'mean_aktivitas': float(np.mean(X_train[:, 1])),
        'mean_hp': float(np.mean(y_train))
    })

@app.route('/dataset')
def get_dataset():
    """Endpoint untuk mendapatkan dataset training"""
    dataset = []
    for i in range(min(100, len(X_train))):
        dataset.append({
            'tidur': float(X_train[i][0]),
            'aktivitas': float(X_train[i][1]),
            'hp': float(y_train[i])
        })
    return jsonify(dataset)

@app.route('/history')
def get_history():
    """Endpoint untuk mendapatkan history prediksi"""
    return jsonify(prediction_history)

@app.route('/export/history')
def export_history():
    """Export history ke CSV"""
    if not prediction_history:
        return jsonify({'error': 'Tidak ada data untuk diexport'}), 400
    
    # Buat CSV
    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(['Timestamp', 'Jam Tidur', 'Jam Aktivitas', 'Prediksi HP', 'Kategori'])
    
    for entry in prediction_history:
        writer.writerow([
            entry['timestamp'],
            entry['tidur'],
            entry['aktivitas'],
            entry['prediksi'],
            entry['kategori']
        ])
    
    # Convert to bytes
    output = BytesIO()
    output.write(si.getvalue().encode('utf-8'))
    output.seek(0)
    
    return send_file(
        output,
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'history_prediksi_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    )

@app.route('/export/dataset')
def export_dataset():
    """Export dataset training ke CSV"""
    # Buat CSV
    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(['Jam Tidur', 'Jam Aktivitas', 'Jam HP'])
    
    for i in range(len(X_train)):
        writer.writerow([
            X_train[i][0],
            X_train[i][1],
            y_train[i]
        ])
    
    # Convert to bytes
    output = BytesIO()
    output.write(si.getvalue().encode('utf-8'))
    output.seek(0)
    
    return send_file(
        output,
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'dataset_training_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    )

@app.route('/statistics')
def get_statistics():
    """Endpoint untuk statistik lengkap"""
    return jsonify({
        'dataset': {
            'total': len(X_train),
            'tidur': {
                'min': float(np.min(X_train[:, 0])),
                'max': float(np.max(X_train[:, 0])),
                'mean': float(np.mean(X_train[:, 0])),
                'std': float(np.std(X_train[:, 0]))
            },
            'aktivitas': {
                'min': float(np.min(X_train[:, 1])),
                'max': float(np.max(X_train[:, 1])),
                'mean': float(np.mean(X_train[:, 1])),
                'std': float(np.std(X_train[:, 1]))
            },
            'hp': {
                'min': float(np.min(y_train)),
                'max': float(np.max(y_train)),
                'mean': float(np.mean(y_train)),
                'std': float(np.std(y_train))
            }
        },
        'model': {
            'r2_score': float(model.score(X_train, y_train)),
            'mse': float(model.mean_squared_error(X_train, y_train)),
            'mae': float(model.mean_absolute_error(X_train, y_train))
        },
        'history': {
            'total_predictions': len(prediction_history)
        }
    })

if __name__ == '__main__':
    print("=" * 60)
    print("🎯 Model Regresi Linier - Prediksi Penggunaan HP")
    print("=" * 60)
    print(f"📊 Dataset: {len(X_train)} samples")
    print(f"📐 Intercept: {model.intercept:.4f}")
    print(f"📉 Koefisien Tidur: {model.coefficients[0]:.4f}")
    print(f"📉 Koefisien Aktivitas: {model.coefficients[1]:.4f}")
    print(f"✅ R² Score: {model.score(X_train, y_train):.4f}")
    print(f"📍 MSE: {model.mean_squared_error(X_train, y_train):.4f}")
    print(f"📍 MAE: {model.mean_absolute_error(X_train, y_train):.4f}")
    print("=" * 60)
    print("\n🚀 Server berjalan di http://127.0.0.1:5000")
    print("=" * 60)
    print("\n📌 Endpoints:")
    print("  - GET  /                  → Halaman utama")
    print("  - POST /predict           → Prediksi penggunaan HP")
    print("  - GET  /model-info        → Informasi model")
    print("  - GET  /dataset           → Dataset training")
    print("  - GET  /history           → History prediksi")
    print("  - GET  /statistics        → Statistik lengkap")
    print("  - GET  /export/history    → Export history ke CSV")
    print("  - GET  /export/dataset    → Export dataset ke CSV")
    print("=" * 60)
    
    app.run(debug=True)