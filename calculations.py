def count_letter(text, letter):
    #Wylicza ilość liter w tekście
    return text.lower().count(letter.lower())

def is_in_range(number, x, y):
    #Sprawdza czy liczba jest w przedziale
    return x <= number <= y