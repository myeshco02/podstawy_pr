#program który oblicza odległość do horyzontu z podpunktami


import math

#wysokosc klawiatury przyjalem jako 1.1
#Wysokosc osoby ok 185cm
#Wysokość wzroku jest zazwyczaj niższa od wzrostu o około 10–12 cm (mam zrodlo)

h = [1.1, 1.75, 20] #m 
#element 0 to wysokosc klawiatury
#element 1 to wysokosc wzroku
#element 2 to wysokosc 20m

d0 = 3.57 * math.sqrt(h[0])
d1 = 3.57 * math.sqrt(h[1])
d2 = 3.57 * math.sqrt(h[2])

print ('Odległość do horyzontu z wysokosci klawiatury wynosi', round(d0, 3), 'km')
print ('Odległość do horyzontu z wysokosci  wzroku', round(d1, 3), 'km')
print ('Odległość do horyzontu z wysokosci 20m-budynku wynosi', round(d2, 3), 'km')