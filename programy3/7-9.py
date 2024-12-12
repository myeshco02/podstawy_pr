from fun8_11 import sum_digits

# Wprowadzenie liczby i parametru 'even'
number = int(input("Enter a number: "))
even = input("Sum even digits? (yes/no): ").strip().lower() == "yes"

# Obliczanie sumy cyfr
result = sum_digits(number, even)
if even:
    print(f"The sum of even digits in {number} is {result}.")
else:
    print(f"The sum of odd digits in {number} is {result}.")
