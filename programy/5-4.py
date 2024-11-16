#program calculating VAT from put in amount
#dane w księgowości muszą być zawsze precyzyjne co do grosza, centa
#stąd wartość powinna mieć maksymalnie 2 miejsca po przecinku


netto_string = input('Podaj kwotę w PLN: ')

netto = float(netto_string)

if netto == round(netto, 2):
    vat = round(netto * 0.23, 2)
    brutto = netto + vat

    print(f"""
Dla kwoty: {netto: ,.2f} PLN
Kwota VAT wynosi: {vat: ,.2f} PLN
Kwota brutto wynosi: {brutto: ,.2f} PLN
    """)

else:
    print('Podano niewłaściwą wartość')