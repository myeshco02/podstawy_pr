import json

# Otwieranie pliku JSON w trybie odczytu
with open('computer.json', 'r', encoding='utf-8') as file:
    # Wczytywanie danych z pliku JSON do zmiennej
    data = json.load(file)

# Drukowanie danych z pliku JSON
print("Informacje o komputerze:")
for key, value in data.items():
    print(f"{key}: {value}")
