import requests
import json

# Pobierz dane o kursach euro z API NBP
url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/last/10?format=json"
response = requests.get(url)
data = response.json()

# Zapisz dane do pliku euro.json
with open('euro.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

# Wyświetlanie danych w formacie tabelarycznym
print("Date            Buying Rate     Selling Rate")
print("=" * 40)

for item in data['rates']:
    date = item['effectiveDate']
    mid_rate = item['mid']
    print(f"{date}      {mid_rate}")

"""Jeśli program nie chce się uruchomić, trzeba w wierszu polecenia wpisać: pip install requests, wtedy powinno zadziałać"""