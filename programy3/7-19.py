def f(number):
    # Zamieniamy liczbę na string, aby łatwiej iterować po cyfrach
    number_str = str(number)
    
    # Słownik do zliczania wystąpień każdej cyfry
    digit_count = {}
    
    # Iteracja po cyfrach i zliczanie ich wystąpień
    for digit in number_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
    
    # Obliczamy sumę cyfr, które powtarzają się
    repeating_sum = sum(int(digit) * count for digit, count in digit_count.items() if count > 1)
    
    return repeating_sum
print(f(1027))      # wynik: 0 (żadna cyfra się nie powtarza)
print(f(230335))    # wynik: 9 (cyfry 3 występują 2 razy, 3 * 2 = 6; cyfry 0 występują 2 razy, 0 * 2 = 0; suma: 9)
print(f(513553007)) # wynik: 21 (cyfry 5 występują 2 razy, 5 * 2 = 10; cyfry 3 występują 2 razy, 3 * 2 = 6; cyfry 0 występują 2 razy, 0 * 2 = 0; suma: 10 + 6 + 0 = 21)
