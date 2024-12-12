def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    
    return b

print(f(5))  # wynik: 5 (ciąg: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...)
print(f(9))  # wynik: 34 (ciąg: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...)

#Inne wyniki niż w przykładzie bo liczenie zaczyna się od 0, a nie od 1
