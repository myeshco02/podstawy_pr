def f(x, y):
    total = 0
    for num in range(x, y + 1):
        if num % 2 == 0 and num % 3 == 0 and num % 4 != 0:
            total += num
    return total


print(f(1, 20))  # wynik: 24
# Liczby spełniające warunki: 6, 18 (6 + 18 = 24)

print(f(10, 30)) # wynik: 48
# Liczby spełniające warunki: 18, 30 (18 + 30 = 48)
