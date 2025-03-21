def f(x):
    # Kökü bulunacak fonksiyon
    return x**3 - x - 2

def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Bisection yöntemi uygulanamaz.")
        return None

    c = a
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            break  # Tam kök bulundu
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

# Başlangıç aralığı ve tolerans değeri
a = 1
b = 2
tolerance = 1e-6

root = bisection(a, b, tolerance)
print(f"Kök yaklaşık olarak: {root}")