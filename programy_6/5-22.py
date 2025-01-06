import json

# Inicjalizacja pustego słownika, w którym będą przechowywane dane produktu
product = {}

# Pobieranie danych od użytkownika
product["name"] = input("Podaj nazwę produktu: ")

# Pobieranie ceny, konwersja na float z dwoma miejscami po przecinku
while True:
    try:
        product["price"] = round(float(input("Podaj cenę produktu (liczba rzeczywista, np. 19.99): ")), 2)
        break
    except ValueError:
        print("Nieprawidłowa cena. Wprowadź liczbę.")

# Pobieranie informacji, czy zapłacono
while True:
    paid = input("Czy zapłacono? (tak/nie): ").strip().lower()
    if paid == "tak":
        product["paid"] = True
        break
    elif paid == "nie":
        product["paid"] = False
        break
    else:
        print("Proszę wpisać 'tak' lub 'nie'.")

# Określenie nazwy pliku do zapisania danych
file_name = "product.json"

# Zapisanie danych produktu do pliku JSON
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(product, file, indent=4)

print("Dane produktu zostały zapisane do pliku", file_name)
