def f(product_code):
    # Sprawdzamy, czy kod składa się dokładnie z 4 cyfr
    if len(product_code) != 4 or not product_code.isdigit():
        return False
    
    # Podział na pierwsze trzy cyfry i cyfrę kontrolną
    first_three = product_code[:3]
    control_digit = int(product_code[3])
    
    # Obliczenie sumy pierwszych trzech cyfr
    sum_of_digits = sum(int(digit) for digit in first_three)
    
    # Sprawdzenie poprawności cyfry kontrolnej
    return sum_of_digits % 7 == control_digit

print(f("1082"))  # True: (1+0+8) % 7 == 2
print(f("2035"))  # True: (2+0+3) % 7 == 5
print(f("1114"))  # False: (1+1+1) % 7 != 4
print(f("7071"))  # False: (7+0+7) % 7 != 1
