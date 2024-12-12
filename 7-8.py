from fun8_11 import min_coins

# Wprowadzenie kwoty do zapłaty
amount_to_pay = int(input("Enter the amount to pay: "))

# Obliczanie minimalnej liczby monet
result = min_coins(amount_to_pay)
print(f"Minimum number of coins needed: {result}")