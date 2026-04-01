# Fungsi: f(x) = x^5 - 3x^4 - 2x^3 + 9x^2 - 10x + 1
def f(x):
    return x**5 - 3*x**4 - 2*x**3 + 9*x**2 - 10*x + 1

def bisection(a, b, tol=1e-6, max_iter=100, mode='tolerance'):
    """
    Metode Bisection dengan 2 mode:
    - mode='tolerance'  -> berhenti saat error < tol
    - mode='iteration'  -> berhenti setelah max_iter iterasi
    """
    fa = f(a)
    fb = f(b)
    
    if fa * fb >= 0:
        print(f"f({a}) = {fa}, f({b}) = {fb}")
        print("Error: Interval tidak valid! f(a) dan f(b) harus berlawanan tanda.")
        return None, 0
    
    iterasi = 0
    
    print(f"{'Iterasi':<6} {'a':<15} {'b':<15} {'c':<15} {'f(c)':<15} {'Error':<15}")
    print("-" * 75)
    
    while True:
        iterasi += 1
        
        # Interval halving
        c = (a + b) / 2
        fc = f(c)
        error = abs(b - a) / 2
        
        print(f"{iterasi:<6} {a:<15.8f} {b:<15.8f} {c:<15.8f} {fc:<15.8f} {error:<15.2e}")
        
        if mode == 'tolerance' and error < tol:
            break
        elif mode == 'iteration' and iterasi >= max_iter:
            break
        
        # Update interval
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    return c, iterasi

# Tampilkan fungsi
print("FUNGSI: f(x) = x^5 - 3x^4 - 2x^3 + 9x^2 - 10x + 1")
print("=" * 75)

# Mode 1: Berdasarkan toleransi
print("\nMODE 1 - Toleransi:\n")
root1, iter1 = bisection(0, 1, tol=1e-6, mode='tolerance')
if root1 is not None:
    print(f"\nAkar: {root1:.10f}")
    print(f"Iterasi: {iter1}")
    print(f"f(x): {f(root1):.2e}\n")

# Mode 2: Berdasarkan jumlah iterasi
print("MODE 2 - 10 Iterasi:\n")
root2, iter2 = bisection(0, 1, max_iter=10, mode='iteration')
if root2 is not None:
    print(f"\nAkar: {root2:.10f}")
    print(f"Iterasi: {iter2}")
    print(f"f(x): {f(root2):.2e}")