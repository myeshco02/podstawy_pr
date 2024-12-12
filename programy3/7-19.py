def f(number):
    number_str = str(number)  # Konwertujemy liczbę na ciąg znaków
    digit_count = {}  # Słownik do zliczania wystąpień cyfr
    sum_repeated_digits = 0  # Zmienna do sumowania powtarzających się cyfr
    
    # Zliczamy wystąpienia każdej cyfry
    for digit in number_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
    
    # Sprawdzamy, które cyfry występują więcej niż raz
    for digit, count in digit_count.items():
        if count > 1:
            sum_repeated_digits += int(digit) * (count - 1)  # Dodajemy powtarzające się cyfry
    
    return sum_repeated_digits

print(f(1027))      # wynik: 0 (żadna cyfra się nie powtarza)
print(f(230335))    # wynik: 9 (cyfry 3 występują 2 razy, 3 * 2 = 6; cyfry 0 występują 2 razy, 0 * 2 = 0; suma: 9)
print(f(513553007)) # wynik: 21 (cyfry 5 występują 2 razy, 5 * 2 = 10; cyfry 3 występują 2 razy, 3 * 2 = 6; cyfry 0 występują 2 razy, 0 * 2 = 0; suma: 10 + 6 + 0 = 21)
