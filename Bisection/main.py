def f(x):
    return x**3 - 3*x + 1

def bisection(a, b, tol=1e-6):
    iterasi = 0
    while (b - a) / 2 > tol:
        iterasi += 1
        c = (a + b) / 2
        if f(c) == 0:
            return c, iterasi
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, iterasi

# Jalankan
root, n_iter = bisection(0, 1)
print(f"Akar: {root}")
print(f"f(x): {f(root)}")
print(f"Jumlah iterasi: {n_iter}")