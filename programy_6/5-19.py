import json

# Funkcja do wczytania danych z pliku
def load_reservations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['reservations']

# Funkcja do liczenia liczby pokoi
def count_rooms(reservations):
    return len(reservations)

# Funkcja do liczenia liczby opłaconych rezerwacji
def count_paid_reservations(reservations):
    return sum(1 for reservation in reservations if reservation['paid'])

# Funkcja do liczenia liczby nieopłaconych rezerwacji
def count_unpaid_reservations(reservations):
    return sum(1 for reservation in reservations if not reservation['paid'])

# Funkcja do obliczania łącznej wartości opłaconych rezerwacji
def total_paid(reservations):
    return sum(reservation['price_per_night'] * reservation['nights'] 
               for reservation in reservations if reservation['paid'])

# Funkcja do obliczania łącznej wartości nieopłaconych rezerwacji
def total_unpaid(reservations):
    return sum(reservation['price_per_night'] * reservation['nights'] 
               for reservation in reservations if not reservation['paid'])

# Funkcja do wyświetlania podsumowania
def print_summary(reservations):
    print(f"Liczba pokoi: {count_rooms(reservations)}")
    print(f"Liczba opłaconych rezerwacji: {count_paid_reservations(reservations)}")
    print(f"Liczba nieopłaconych rezerwacji: {count_unpaid_reservations(reservations)}")
    print(f"Łączna wartość opłaconych rezerwacji: {total_paid(reservations):.2f} PLN")
    print(f"Łączna wartość nieopłaconych rezerwacji: {total_unpaid(reservations):.2f} PLN")

# Główna funkcja
def main():
    # Wczytanie danych
    reservations = load_reservations('reservations.json')
    
    # Wydrukowanie podsumowania
    print_summary(reservations)

# Uruchomienie programu
if __name__ == "__main__":
    main()
