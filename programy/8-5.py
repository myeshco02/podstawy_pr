###
# A program that reads a SWIFT code from the keyboard
# and prints the bank code and country code.
#
swift = input('Podaj kod SWIFT banku: ')
print(f'Bank Code: {swift[0:4]}')
print(f'Country Code: {swift[4:6]}')
#Pamietamy że przy cięciu stringów drugi indeks nie jest wliczany
#Jest to wygodne, bo indeksy zaczynają się od zera, więc jeśli chcemy 4 pierwsze
#to wpisujemy 4 mimo że ostatni wypisany element będzie miał indeks 3 :)