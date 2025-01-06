import csv

def load_provinces(filename):
    """Wczytuje województwa i odpowiadające im litery z pliku CSV."""
    provinces = {}
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Pomijamy pierwszy wiersz, który zawiera nagłówek
        for row in reader:
            # Pierwsza kolumna: litera, Druga kolumna: województwo
            provinces[row[0]] = row[1]
    return provinces

def count_vehicles_by_province(vehicle_file, provinces):
    """Zlicza pojazdy według województw na podstawie numerów rejestracyjnych."""
    province_count = {province: 0 for province in provinces.values()}
    
    with open(vehicle_file, 'r', encoding='utf-8') as file:
        for line in file:
            vehicle_number = line.strip()
            if vehicle_number:  # Sprawdź, czy linia nie jest pusta
                first_letter = vehicle_number[0]
                # Dopasuj literę do województwa
                if first_letter in provinces:
                    province = provinces[first_letter]
                    province_count[province] += 1
    return province_count

def main():
    # Wczytaj dane o województwach z pliku province.csv
    provinces = load_provinces('province.csv')
    
    # Zlicz pojazdy według województw na podstawie vehicle.txt
    vehicle_counts = count_vehicles_by_province('vehicle.txt', provinces)
    
    # Wyświetl wyniki
    print("Liczba pojazdów zarejestrowanych w poszczególnych województwach:")
    for province, count in vehicle_counts.items():
        print(f"{province}: {count}")

if __name__ == "__main__":
    main()
