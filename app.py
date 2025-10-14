from flask import Flask, render_template
import pandas as pd
import numpy as np
import json

# Inisialisasi aplikasi Flask
app = Flask(__name__)

def calculate_regression():
    """Fungsi untuk membaca data dari CSV dan menghitung regresi."""
    
    # --- BAGIAN YANG DIUBAH ---
    # Sekarang membaca langsung dari file, bukan string
    file_path = 'data/hp_usage.csv'
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        # Mengembalikan error jika file tidak ditemukan
        return {"error": f"File '{file_path}' tidak ditemukan."}
    # --- AKHIR BAGIAN YANG DIUBAH ---

    # Menyiapkan matriks X dan Y
    df['intercept'] = 1
    X = df[['intercept', 'TidurJam', 'AktivitasJam']].values
    Y = df['HPJam'].values.reshape(-1, 1)
    
    # Menghitung koefisien beta
    try:
        XT = X.T
        XTX = XT @ X
        XTX_inv = np.linalg.inv(XTX)
        XTY = XT @ Y
        beta_coeffs = XTX_inv @ XTY
    except np.linalg.LinAlgError:
        return {"error": "Perhitungan matriks gagal (singular matrix)."}

    # Menyiapkan data untuk dikirim ke template
    results = {
        "beta0": beta_coeffs[0][0],
        "beta1": beta_coeffs[1][0],
        "beta2": beta_coeffs[2][0],
        "plot_data": {
            "tidur": df['TidurJam'].tolist(),
            "aktivitas": df['AktivitasJam'].tolist(),
            "hp": df['HPJam'].tolist()
        }
    }
    return results

@app.route('/')
def dashboard():
    """Halaman utama yang akan menampilkan dashboard."""
    regression_results = calculate_regression()
    
    # Jika ada error saat kalkulasi, tampilkan pesan error
    if "error" in regression_results:
        return f"<h1>Terjadi Error</h1><p>{regression_results['error']}</p>", 500
    
    # Kirim hasil perhitungan ke file HTML
    return render_template('index.html',
                           beta0=regression_results['beta0'],
                           beta1=regression_results['beta1'],
                           beta2=regression_results['beta2'],
                           plot_data=json.dumps(regression_results['plot_data'])
                          )

if __name__ == '__main__':
    # Menjalankan server di semua antarmuka jaringan di port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)