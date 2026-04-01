from sympy import symbols, diff, lambdify, pprint

# Buat fungsi dan turunannya secara otomatis
x = symbols('x')
f_sym = x**5 - 3*x**4 - 2*x**3 + 9*x**2 - 10*x + 1
df_sym = diff(f_sym, x)

pprint(f_sym)
print("--------------------------")
pprint(df_sym)

# Konversi ke fungsi Python yang bisa dipanggil
f = lambdify(x, f_sym, 'numpy')
df = lambdify(x, df_sym, 'numpy')

def newton_raphson(x0, tol=1e-6, max_iter=100, mode='tolerance'):
    """
    mode='tolerance'  -> berhenti saat error < tol
    mode='iteration'  -> berhenti setelah max_iter iterasi
    """
    x = x0
    iterasi = 0
    
    print(f"{'Iterasi':<6} {'x':<15} {'f(x)':<15} {'Δx':<15}")
    print("-" * 50)
    
    while True:
        iterasi += 1
        fx = f(x)
        dfx = df(x)
        
        if abs(dfx) < 1e-10:
            print("Turunan mendekati nol!")
            break
        
        x_new = x - fx / dfx
        dx = abs(x_new - x)
        
        print(f"{iterasi:<6} {x:<15.8f} {fx:<15.8f} {dx:<15.8f}")
        
        if mode == 'tolerance' and dx < tol:
            break
        elif mode == 'iteration' and iterasi >= max_iter:
            break
        
        x = x_new
    
    return x_new, iterasi

# Mode 1: Berdasarkan toleransi
print("MODE 1 - Toleransi:\n")
root1, iter1 = newton_raphson(0.5, tol=1e-6, mode='tolerance')
print(f"\nAkar: {root1:.10f}, Iterasi: {iter1}, f(x): {f(root1):.2e}\n")

# Mode 2: Berdasarkan jumlah iterasi
print("MODE 2 - 5 Iterasi:\n")
root2, iter2 = newton_raphson(0.5, max_iter=10, mode='iteration')
print(f"\nAkar: {root2:.10f}, Iterasi: {iter2}, f(x): {f(root2):.2e}")