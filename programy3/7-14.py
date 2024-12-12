def f(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2
    else:
        raise ValueError("Unsupported operator")

print(f(2, 3, "+"))   # wynik: 5
print(f(2, 3, "%"))   # wynik: 2
print(f(2, 3, "**"))  # wynik: 8
print(f(2, 3, "*"))   # wynik: 6
print(f(2, 3, "-"))   # wynik: -1

""" Pobranie danych od użytkownika
try:
    number1 = float(input("Podaj pierwszą liczbę: "))
    number2 = float(input("Podaj drugą liczbę: "))
    operator = input("Podaj operator (+, -, *, %, **): ")

    # Wywołanie funkcji i wyświetlenie wyniku
    result = f(number1, number2, operator)
    print(f"Wynik operacji {number1} {operator} {number2} to: {result}")
except ValueError as e:
    print(f"Błąd: {e}") """
