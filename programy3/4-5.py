###
# Calculates the final grade for a test based
# on the number of points obtained
#
import math

# Funkcja obliczająca ocenę końcową
def pts_to_grade(points):
    grade = ''
    if points < 10:
        grade = 'Niedostateczny'
    elif points < 14:
        grade = 'Dostateczny'
    elif points < 18:
        grade = 'Dobry'
    else:
        grade = 'Bardzo dobry'
    return grade

# Program główny
def main():
    print("Program oblicza ocenę końcową na podstawie liczby punktów.")
    try:
        # Odczyt liczby punktów od użytkownika
        points = int(input("Podaj liczbę uzyskanych punktów: "))
        if points < 0:
            print("Liczba punktów nie może być ujemna.")
        else:
            # Obliczenie oceny końcowej
            grade = pts_to_grade(points)
            print(f"Liczba punktów: {points} - Ocena końcowa: {grade}")
    except ValueError:
        print("Podano nieprawidłowe dane. Proszę podać liczbę całkowitą.")

# Wywołanie programu głównego
main()
