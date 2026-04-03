# Numerical Methods

Kumpulan implementasi metode numerik menggunakan Python, dibuat sebagai tugas mata kuliah **Komputasi Numeris** — Universitas Gadjah Mada.

---

## Struktur Repository

```
Numerical_Methods/
├── Non-linear_Solution/
│   ├── Bisection.ipynb
│   ├── Newton_Raphson.ipynb
│   └── Secant.ipynb
├── Linear_Solution/
│   ├── Gauss_Elimination.ipynb
│   ├── Gauss_Jordan_Elimination.ipynb
│   ├── Gauss_Seidel_Iteration.ipynb
│   └── Jacobi_Iteration.ipynb
├── Least_Square_Regression/
│   └── Least_Squares.ipynb
└── Interpolation/
    ├── Newtons_Interpolation.ipynb
    └── Lagrange_Interpolation.ipynb
```

---

## Daftar Metode

### 1. Non-linear Solution

Metode pencarian akar persamaan non-linear $f(x) = 0$.

| Notebook | Metode | Deskripsi |
|---|---|---|
| `Bisection.ipynb` | Bisection | Pencarian akar dengan pembagian interval (halving) |
| `Newton_Raphson.ipynb` | Newton-Raphson | Pencarian akar menggunakan turunan fungsi |
| `Secant.ipynb` | Secant | Pencarian akar tanpa turunan eksplisit (aproksimasi finite difference) |

### 2. Linear Solution

Metode penyelesaian sistem persamaan linear $Ax = b$.

| Notebook | Metode | Deskripsi |
|---|---|---|
| `Gauss_Elimination.ipynb` | Gaussian Elimination | Forward elimination + backward substitution |
| `Gauss_Jordan_Elimination.ipynb` | Gauss-Jordan Elimination | Eliminasi hingga matriks identitas, tanpa back substitution |
| `Gauss_Seidel_Iteration.ipynb` | Gauss-Seidel Iteration | Metode iteratif, memperbarui nilai secara langsung tiap iterasi |
| `Jacobi_Iteration.ipynb` | Jacobi Iteration | Metode iteratif, memperbarui semua nilai serentak tiap iterasi |

### 3. Least Square Regression

Metode fitting kurva menggunakan pendekatan kuadrat terkecil.

| Notebook | Metode | Deskripsi |
|---|---|---|
| `Least_Squares.ipynb` | Least Squares | Fitting kurva terhadap data dengan meminimalkan jumlah kuadrat error, di dalamnya berisi Least Square Linear, Multiple Linear, Polynomial, dan Non-linear|

### 4. Interpolation

Metode pencarian nilai estimasi dari sekumpulan titik data yang diketahui.

| Notebook | Metode | Deskripsi |
|---|---|---|
| `Newtons_Interpolation.ipynb` | Newton's Divided Difference | Interpolasi menggunakan tabel divided difference |
| `Lagrange_Interpolation.ipynb` | Lagrange Interpolation | Interpolasi menggunakan basis polinomial Lagrange |

---

## Persyaratan / Dependencies

Python 3.12 dan library berikut:

```bash
pip install numpy sympy matplotlib
```

| Library      | Versi  |
|--------------|--------|
| `numpy`      | 2.4.2  | 
| `sympy`      | 1.14.0 |
| `matplotlib` | 3.10.8 |

---

## Cara Penggunaan

Clone repository ini:

```bash
git clone https://github.com/Verrald/Numerical_Methods
```

Masuk ke folder metode yang diinginkan dan jalankan notebook:

```bash
cd Non-linear_Solution
jupyter notebook Bisection.ipynb
```

---

## Disclaimer
Beberapa proses tidak tertampil di branch main, tapi ada di dalam brach yang ada di repository ini, hal ini terjadi karena kesalahan saat awal membuat folder, harapan ingin membuat folder namun malah jadi membuat branch baru, sehingga terlihat kontribusi (history commits) tidak lengkap. untuk konfirmasi bisa lihat Brach yang ada (Bisection, Gauss_Method, dan Newton_Raphson_Method), terima kasih.

## Informasi

- Nama: Muhammad Haryo Setiawan
- NIM: 25/558273/PTK/16529
- Mata Kuliah: Komputasi Numeris
- Dosen Pengampu: Ir. Roni Irnawan, S.T., M.Sc., Ph.D., SMIEEE.
- Program Studi: Magister Teknik Elektro
- Universitas Gadjah Mada