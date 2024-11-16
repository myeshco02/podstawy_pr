###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results

import math #importujemy żeby mieć dokładne pi

while True: #petla sprawdza czy dobra liczba 
    r_str = (input("Podaj promień koła: "))
    r = float(r_str) #konwersja str na float

    if r <= 0:
        print("Podaj liczbę nieujemną!") #W przypadku wprowadzenia złej liczby
    else:
        c = 2 * math.pi * r #obliczenie obwodu
        a = math.pi * r ** 2 #obliczenie pola powierzchni
        break



print(f"""Obwód koła wynosi: {c: ,.2f} 
Pole powierzchni koła wynosi: {a: ,.2f}
      """) #wypisanie wyników z dokładnością 2 miejsc po przecinku