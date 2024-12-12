def power(x, n):
    # Warunek bazowy
    if n == 0:
        return 1
    # Rekurencja
    return x * power(x, n - 1)

# Obliczenie 5^3
x = 5
n = 3
result = power(x, n)
print(f"{x} do potęgi {n} wynosi {result}")
