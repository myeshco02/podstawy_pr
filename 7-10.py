from fun8_11 import count_negative_evens

# Wprowadzenie zakresu
x = int(input("Enter the start of the range: "))
y = int(input("Enter the end of the range: "))

# Obliczanie liczby ujemnych liczb parzystych
result = count_negative_evens(x, y)
print(f"The count of negative even numbers in the range <{x}, {y}> is {result}.")