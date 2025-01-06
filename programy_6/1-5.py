# Tablica z 5 słownikami
countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 67000000},
    {"name": "Italy", "population": 59000000},
    {"name": "Spain", "population": 47000000}
]

# Nagłówek tabeli
print(f"{'COUNTRY':<10} {'POPULATION':<10}")

# Iteracja przez tablicę i wyświetlanie zawartości
for country in countries:
    print(f"{country['name']:<10} {country['population']:<10}")
