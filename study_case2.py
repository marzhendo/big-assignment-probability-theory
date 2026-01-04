import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

# --- PARAMETER STUDI KASUS 2 (AMBULANS) ---
rata_rata = 1.2     # Lambda = 12 permintaan / 10 jam
total_jam = 10

# Data Pengamatan (Dari Tabel Ambulans)
# 0 permintaan: 2 kali (Jam 2, 6)
# 1 permintaan: 5 kali (Jam 1, 4, 5, 9, 10)
# 2 permintaan: 2 kali (Jam 3, 7)
# 3 permintaan: 1 kali (Jam 8)
data_ambulans = {
    0: 2,
    1: 5,
    2: 2,
    3: 1
}

# --- PERHITUNGAN ---
x = np.arange(0, 6) # Rentang X lebih kecil karena datanya sedikit (0-5)
peluang_teori = poisson.pmf(x, rata_rata)

peluang_data = np.zeros_like(x, dtype=float)
for jml, freq in data_ambulans.items():
    if jml < len(peluang_data):
        peluang_data[jml] = freq / total_jam

# --- GRAFIK ---
plt.figure(figsize=(8, 5))
lebar = 0.35

plt.bar(x - lebar/2, peluang_data, lebar, label='Data Pengamatan', color='#48C9B0', edgecolor='black')
plt.bar(x + lebar/2, peluang_teori, lebar, label='Teori Poisson (λ=1.2)', color='#F4D03F', alpha=0.9, edgecolor='black')
plt.plot(x, peluang_teori, color='#C0392B', marker='o', linestyle='--', label='Kurva Teori')

plt.xlabel('Jumlah Permintaan Ambulans per Jam')
plt.ylabel('Peluang')
plt.title('Studi Kasus 2: Kebutuhan Ambulans Shift Malam')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.savefig('grafik_ambulans.png')
plt.show()