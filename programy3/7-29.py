def factorial(n):
    # Warunek bazowy
    if n == 0 or n == 1:
        return 1
    # Rekurencja
    if n > 1:
        return n * factorial(n - 1)

# Obliczenie silni dla n = 5
n = 8
result = factorial(n)
print(f"Silnia {n}! wynosi {result}")
