def hide(card_number):
    #Ukrywa numer karty zostawiając dwie pierwsze i cztery ostatnie cyfry
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Card number must be a 16-digit string.")
    return card_number[:2] + '*' * 10 + card_number[-4:]

