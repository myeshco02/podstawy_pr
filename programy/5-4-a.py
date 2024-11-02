#program 5-4 ale lepszy
while True:
    netto_string = input('Podaj kwotę w PLN: ')

    try:
        # Sprawdzamy czy przypadkiem nie wprowadzono liter lub innych znaków
        netto = float(netto_string)
        #jak wszystko ok idziemy dalej jak nie to przechodzi do except i zaczyna od nowa

        # Sprawdzenie liczby miejsc po przecinku
        if netto != round(netto, 2):
            print("Podano niewłaściwą wartość. Wprowadź liczbę z maksymalnie dwoma miejscami po przecinku.")
            continue  # Wraca do początku pętli
        
        else:
            # Obliczenia
            vat = round(netto * 0.23, 2)
            brutto = netto + vat

        # Wynik z formatowaniem
            print(f"""
Dla kwoty: {netto: ,.2f} PLN
Kwota VAT wynosi: {vat: ,.2f} PLN
Kwota brutto wynosi: {brutto: ,.2f} PLN
        """)
            break  # Jeśli wszystko jest poprawne, przerywamy pętlę

    except ValueError:
        print("Podano niewłaściwą wartość. Upewnij się, że wprowadzasz liczbę.")