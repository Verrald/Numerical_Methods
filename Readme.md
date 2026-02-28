# Newton-Raphson Method 

Program Python untuk mencari akar persamaan non-linear menggunakan **Metode Newton-Raphson** dengan bantuan library `sympy` untuk kalkulus simbolik.

## 📖 Deskripsi

Program ini mengimplementasikan metode Newton-Raphson untuk menemukan akar dari fungsi polinomial. Keunggulan program ini adalah kemampuan untuk menghitung turunan fungsi secara otomatis menggunakan `sympy`, sehingga pengguna tidak perlu menghitung turunan secara manual.

## ✨ Fitur

- ✅ **Turunan Otomatis** - Menggunakan `sympy.diff()` untuk menghitung turunan fungsi secara simbolik
- ✅ **Dua Mode Perhitungan**:
  - **Mode Toleransi** - Berhenti ketika error < nilai toleransi yang ditentukan
  - **Mode Iterasi** - Berhenti setelah jumlah iterasi maksimum tercapai
- ✅ **Tabel Iterasi** - Menampilkan proses konvergensi secara detail (Iterasi, x, f(x), Δx)
- ✅ **Visualisasi Fungsi** - Menampilkan fungsi dan turunannya dalam format matematika yang rapi
- ✅ **Konversi Numerik** - Menggunakan `lambdify` untuk evaluasi fungsi yang cepat dengan `numpy`

## 📦 Dependensi

Pastikan Anda telah menginstall Python 3.x dan library berikut:

```bash
pip install sympy numpy

## Cara Instalasi

git clone https://github.com/Verrald/Numerical_Methods_test
cd newton-raphson-solver

## Cara Penggunaan

python main.py

## Kostumisasi Fungsi

Untuk mengubah fungsi yang ingin dicari akarnya, edit bagian berikut dalam kode:

```bash
x = symbols('x')
f_sym = x**5 - 3*x**4 - 2*x**3 + 9*x**2 - 10*x + 1  # Ubah fungsi di sini
df_sym = diff(f_sym, x)  # Turunan dihitung otomatis

## Kostumisasi Parameter

Untuk mengubah parameter sesuai kebutuhan

```bash
## Mode Toleransi
root, iterasi = newton_raphson(x0=0.5, tol=1e-6, mode='tolerance')

## Mode Iterasi
root, iterasi = newton_raphson(x0=0.5, max_iter=10, mode='iteration')

## Tentang Metode Newton-Raphson

Metode Newton-Raphson merupakan metode numerik iteratif untuk menemukan akar dari fungsi f(x) = 0. Rumus iterasinya adalah:

```bash
x_{n+1} = x_n-f(x_n)/f'(x_n)

Keterangan:
- x_n = nilai aproksimasi saat ini
- f(x_n) = nilai fungsi pada x_n
- f'(x_n) = nilai turunan fungsi pada x_n
- x_{n+1} = nilai aproksimasi berikutnya

## Kelebihan

- Konvergensi sangat cepat (kuadratik), dengan catatan nilai tebakan dekat dengan akar.
- Mudah diimplementasikan

## Keterbatasan

- Memerhitungkan turunan fungsi
- Dapat divergen jika tebakan awal (x0) terlalu jauh dari akar sebenarnya
- Gagal jika f'(x) = 0

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](LICENSE) untuk detailnya.