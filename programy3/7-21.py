def f(number1, number2, number3):
    return max(number1, number2, number3) - min(number1, number2, number3)

print(f(7, 4, 9))  # wynik: 5 (9 - 4 = 5)
print(f(2, 12, 8)) # wynik: 10 (12 - 2 = 10)
