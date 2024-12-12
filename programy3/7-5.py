from calculations import is_in_range

# Sprawdzanie, czy liczba jest w zakresie
number = int(input("A number: "))
x, y = 2, 15
in_range = is_in_range(number, x, y)
result = "yes" if in_range else "no"
print(f"Number {number} in the range <{x},{y}>: {result}")
