def f(n):
    return '/'.join('*' for _ in range(n)) #'/'.join(...) łączy elementy tej listy, wstawiając między nimi ukośnik (/).

print(f(4))  # wynik: "*/*/*/*"
print(f(1))  # wynik: "*"