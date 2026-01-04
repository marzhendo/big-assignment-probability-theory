import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

# --- 1. DATA DAN PARAMETER ---
rata_rata = 4       # Nilai Lambda (rata-rata pasien per jam)
total_jam = 10      # Total waktu pengamatan (jam)

# Data dari Tabel: {Jumlah Pasien : Berapa kali terjadi}
data_tabel = {
    2: 1,  # 2 pasien muncul 1 kali
    3: 3,  # 3 pasien muncul 3 kali
    4: 2,  # 4 pasien muncul 2 kali
    5: 3,  # 5 pasien muncul 3 kali
    6: 1   # 6 pasien muncul 1 kali
}

# --- 2. PERHITUNGAN ---
# Sumbu X (angka 0 sampai 11)
x = np.arange(0, 12)

# Hitung Peluang Teori (Rumus Poisson)
peluang_teori = poisson.pmf(x, rata_rata)

# Hitung Peluang Data (Frekuensi Relatif)
peluang_data = np.zeros_like(x, dtype=float)

for pasien, frekuensi in data_tabel.items():
    peluang_data[pasien] = frekuensi / total_jam

# --- 3. MEMBUAT GRAFIK ---
plt.figure(figsize=(10, 6))
lebar = 0.35

# Membuat Grafik Batang (Bar Chart)
plt.bar(x - lebar/2, peluang_data, lebar, label='Data Pengamatan', color='#5DADE2', edgecolor='black')
plt.bar(x + lebar/2, peluang_teori, lebar, label='Teori Poisson (λ=4)', color='#F5B041', alpha=0.9, edgecolor='black')

# Menambahkan Garis Kurva
plt.plot(x, peluang_teori, color='red', marker='o', linestyle='--', label='Kurva Teori')

# Menambahkan Judul dan Label
plt.xlabel('Jumlah Pasien per Jam')
plt.ylabel('Peluang')
plt.title('Perbandingan Data UGD vs Teori Poisson')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Menampilkan Grafik
plt.savefig('grafik_poisson.png')
plt.show()