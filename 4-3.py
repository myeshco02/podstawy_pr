###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math

# Definicja funkcji do obliczenia pola trójkąta za pomocą wzoru Herona
def triangle_area(a, b, c):
    # Obliczenie połowy obwodu
    s = (a + b + c) / 2
    # Obliczenie pola za pomocą wzoru Herona
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Funkcja do wprowadzenia danych i obliczenia pola
def main():
    print("Obliczanie pola trójkąta za pomocą wzoru Herona.")
    # Pobieranie długości boków od użytkownika
    a = float(input("Podaj długość boku a: "))
    b = float(input("Podaj długość boku b: "))
    c = float(input("Podaj długość boku c: "))
    
    # Obliczanie i wyświetlanie wyniku
    area = triangle_area(a, b, c)
    print(f"Pole trójkąta o bokach {a}, {b}, {c} wynosi: {area}")

# Wywołanie funkcji main()
main()
