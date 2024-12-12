def f(n):
    return ''.join(str(i) for i in range(1, n+1))

print(f(11))  # wynik: "1234567891011"
print(f(4))   # wynik: "1234"