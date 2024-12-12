def sum_natural(n):
    # Warunek bazowy
    if n == 0:
        return 0
    # Rekurencja
    return n + sum_natural(n - 1)

# Oblicz sumę liczb naturalnych od 1 do 10
n = 10
result = sum_natural(n)
print(f"Suma liczb naturalnych od 1 do {n} wynosi {result}")
