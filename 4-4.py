###
# Calculates the sum of the digits in a number
#

# Funkcja obliczająca sumę cyfr w liczbie
def sum_digits(number):
    # Użycie wartości bezwzględnej dla obsługi liczb ujemnych
    number = abs(number)
    # Konwersja liczby na ciąg znaków, iteracja po cyfrach i sumowanie
    digit_sum = sum(int(digit) for digit in str(number))
    return digit_sum

# Program główny
def main():
    print("Program oblicza sumę cyfr w podanej liczbie.")
    # Odczyt liczby od użytkownika
    try:
        user_input = int(input("Podaj liczbę całkowitą (dodatnią, ujemną lub zero): "))
        # Obliczenie sumy cyfr
        result = sum_digits(user_input)
        print(f"Suma cyfr liczby {user_input} wynosi: {result}")
    except ValueError:
        print("Podano nieprawidłowe dane. Proszę podać liczbę całkowitą.")

# Wywołanie programu głównego
main()